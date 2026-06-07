from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import PhraseCategory, Phrase
from translations.services import translation_service


@login_required
def phrasebook_home(request):
    """Display all phrasebook categories."""
    categories = PhraseCategory.objects.all()
    return render(request, 'phrasebook/home.html', {'categories': categories})


@login_required
def category_detail(request, slug):
    """Display phrases in a category with optional live translation."""
    category = get_object_or_404(PhraseCategory, slug=slug)
    phrases = category.phrases.all()
    target_lang = request.GET.get('lang', 'es')

    # Build phrase list with selected language translation
    phrase_list = []
    for phrase in phrases:
        translated = phrase.get_translation(target_lang)
        # If no stored translation, try the translation service
        if translated == phrase.source_text and target_lang != 'en':
            if translation_service.is_available():
                result = translation_service.translate(
                    phrase.source_text, target_lang, 'en'
                )
                translated = result['translated_text']
        phrase_list.append({
            'phrase': phrase,
            'translated_text': translated,
        })

    from django.conf import settings
    return render(request, 'phrasebook/category.html', {
        'category': category,
        'phrase_list': phrase_list,
        'target_lang': target_lang,
        'languages': settings.SUPPORTED_LANGUAGES,
    })
