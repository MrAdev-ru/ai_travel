from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

from translations.models import TranslationHistory, FavoriteTranslation
from phrasebook.models import PhraseCategory


@login_required
def home_view(request):
    """
    Dashboard home with translation statistics and quick actions.
    """
    user = request.user
    now = timezone.now()
    week_ago = now - timedelta(days=7)
    month_ago = now - timedelta(days=30)

    # Aggregate statistics
    total_translations = TranslationHistory.objects.filter(user=user).count()
    translations_this_week = TranslationHistory.objects.filter(
        user=user, created_at__gte=week_ago
    ).count()
    translations_this_month = TranslationHistory.objects.filter(
        user=user, created_at__gte=month_ago
    ).count()
    total_favorites = FavoriteTranslation.objects.filter(user=user).count()

    # Most used target languages
    top_languages = (
        TranslationHistory.objects.filter(user=user)
        .values('target_language')
        .annotate(count=Count('id'))
        .order_by('-count')[:5]
    )

    # Map language codes to display names
    from django.conf import settings
    lang_map = dict(settings.SUPPORTED_LANGUAGES)
    for item in top_languages:
        item['language_name'] = lang_map.get(item['target_language'], item['target_language'])

    # Recent activity
    recent_translations = TranslationHistory.objects.filter(user=user)[:8]

    # Phrasebook categories for quick access
    categories = PhraseCategory.objects.all()[:6]

    context = {
        'total_translations': total_translations,
        'translations_this_week': translations_this_week,
        'translations_this_month': translations_this_month,
        'total_favorites': total_favorites,
        'top_languages': top_languages,
        'recent_translations': recent_translations,
        'categories': categories,
        'lang_map': lang_map,
    }
    return render(request, 'dashboard/home.html', context)
