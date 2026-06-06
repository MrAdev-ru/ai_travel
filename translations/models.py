from django.db import models
from django.contrib.auth.models import User


class TranslationHistory(models.Model):
    """
    Stores every translation performed by a user.
    Includes source/target text and detected language information.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='translation_history',
    )
    source_text = models.TextField(help_text='Original text before translation')
    translated_text = models.TextField(help_text='Translated output text')
    source_language = models.CharField(max_length=10, help_text='Source language code')
    target_language = models.CharField(max_length=10, help_text='Target language code')
    detected_language = models.CharField(
        max_length=10,
        blank=True,
        help_text='Auto-detected source language code',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Translation histories'

    def __str__(self):
        preview = self.source_text[:50]
        return f'{self.user.username}: {preview}...'


class FavoriteTranslation(models.Model):
    """
    User-saved favorite translations for quick access.
    Can reference history or store standalone translation data.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite_translations',
    )
    source_text = models.TextField()
    translated_text = models.TextField()
    source_language = models.CharField(max_length=10)
    target_language = models.CharField(max_length=10)
    # Optional link to the original history entry
    history = models.ForeignKey(
        TranslationHistory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='favorites',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        # Prevent duplicate favorites for the same translation
        unique_together = ['user', 'source_text', 'target_language']

    def __str__(self):
        return f'Favorite: {self.source_text[:30]}... ({self.user.username})'
