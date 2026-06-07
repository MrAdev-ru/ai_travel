import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages

from .forms import TranslationForm
from .models import TranslationHistory, FavoriteTranslation
from .services import translation_service


@login_required
def translate_view(request):
    """Main translation page with form and results."""
    form = TranslationForm()
    result = None
    api_available = translation_service.is_available()

    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            source_text = form.cleaned_data['source_text'].strip()
            source_lang = form.cleaned_data['source_language']
            target_lang = form.cleaned_data['target_language']

            if source_text:
                translation = translation_service.translate(
                    source_text,
                    target_lang,
                    source_lang if source_lang != 'auto' else None,
                )

                detected = translation['detected_source_language']
                result = {
                    'source_text': source_text,
                    'translated_text': translation['translated_text'],
                    'source_language': translation['source_language'],
                    'target_language': target_lang,
                    'detected_language': detected,
                }

                # Save to translation history
                history = TranslationHistory.objects.create(
                    user=request.user,
                    source_text=source_text,
                    translated_text=translation['translated_text'],
                    source_language=translation['source_language'],
                    target_language=target_lang,
                    detected_language=detected,
                )
                result['history_id'] = history.id

                if not api_available:
                    messages.warning(
                        request,
                        'Translation service is not configured. Showing demo output.',
                    )

    context = {
        'form': form,
        'result': result,
        'api_available': api_available,
        'recent_history': TranslationHistory.objects.filter(user=request.user)[:5],
    }
    return render(request, 'translations/translate.html', context)


@login_required
def history_view(request):
    """Display full translation history for the current user."""
    history = TranslationHistory.objects.filter(user=request.user)
    return render(request, 'translations/history.html', {'history': history})


@login_required
def favorites_view(request):
    """Display user's favorite translations."""
    favorites = FavoriteTranslation.objects.filter(user=request.user)
    return render(request, 'translations/favorites.html', {'favorites': favorites})


@login_required
@require_POST
def add_favorite_view(request):
    """Add a translation to favorites (AJAX or form POST)."""
    history_id = request.POST.get('history_id')
    source_text = request.POST.get('source_text', '')
    translated_text = request.POST.get('translated_text', '')
    source_language = request.POST.get('source_language', 'en')
    target_language = request.POST.get('target_language', 'es')

    history = None
    if history_id:
        history = get_object_or_404(TranslationHistory, id=history_id, user=request.user)
        source_text = history.source_text
        translated_text = history.translated_text
        source_language = history.source_language
        target_language = history.target_language

    favorite, created = FavoriteTranslation.objects.get_or_create(
        user=request.user,
        source_text=source_text,
        target_language=target_language,
        defaults={
            'translated_text': translated_text,
            'source_language': source_language,
            'history': history,
        },
    )

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'created': created})

    messages.success(request, 'Added to favorites!' if created else 'Already in favorites.')
    return redirect('translations:favorites')


@login_required
@require_POST
def remove_favorite_view(request, pk):
    """Remove a translation from favorites."""
    favorite = get_object_or_404(FavoriteTranslation, pk=pk, user=request.user)
    favorite.delete()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True})

    messages.success(request, 'Removed from favorites.')
    return redirect('translations:favorites')


@login_required
@require_POST
def detect_language_view(request):
    """AJAX endpoint for automatic language detection."""
    try:
        data = json.loads(request.body)
        text = data.get('text', '').strip()
    except json.JSONDecodeError:
        text = request.POST.get('text', '').strip()

    if not text:
        return JsonResponse({'error': 'No text provided'}, status=400)

    detection = translation_service.detect_language(text)
    return JsonResponse(detection)


@login_required
@require_POST
def ajax_translate_view(request):
    """AJAX endpoint for real-time translation."""
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    text = data.get('text', '').strip()
    target_lang = data.get('target_language', 'es')
    source_lang = data.get('source_language', 'auto')

    if not text:
        return JsonResponse({'error': 'No text provided'}, status=400)

    translation = translation_service.translate(
        text,
        target_lang,
        source_lang if source_lang != 'auto' else None,
    )

    # Save to history
    history = TranslationHistory.objects.create(
        user=request.user,
        source_text=text,
        translated_text=translation['translated_text'],
        source_language=translation['source_language'],
        target_language=target_lang,
        detected_language=translation['detected_source_language'],
    )

    return JsonResponse({
        'translated_text': translation['translated_text'],
        'detected_language': translation['detected_source_language'],
        'source_language': translation['source_language'],
        'history_id': history.id,
    })