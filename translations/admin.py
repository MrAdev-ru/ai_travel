from django.contrib import admin
from .models import TranslationHistory, FavoriteTranslation


@admin.register(TranslationHistory)
class TranslationHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'source_language', 'target_language', 'created_at')
    list_filter = ('source_language', 'target_language', 'created_at')
    search_fields = ('source_text', 'translated_text', 'user__username')
    readonly_fields = ('created_at',)


@admin.register(FavoriteTranslation)
class FavoriteTranslationAdmin(admin.ModelAdmin):
    list_display = ('user', 'source_language', 'target_language', 'created_at')
    list_filter = ('source_language', 'target_language')
    search_fields = ('source_text', 'translated_text', 'user__username')
