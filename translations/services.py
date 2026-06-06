"""
Google Cloud Translation API service wrapper.
Handles translation, language detection, and fallback behavior.
"""
import logging

from django.conf import settings

logger = logging.getLogger(__name__)


class TranslationService:
    """Service class for Google Cloud Translation API operations."""

    def __init__(self):
        self._client = None

    @property
    def client(self):
        """Lazy-load the Google Translate client."""
        if self._client is None:
            try:
                from google.cloud import translate_v2 as translate
                self._client = translate.Client()
            except Exception as e:
                logger.warning('Google Translate client unavailable: %s', e)
                self._client = False
        return self._client if self._client else None

    def is_available(self):
        """Check if the translation API is configured and reachable."""
        return self.client is not None

    def detect_language(self, text):
        """
        Detect the language of the given text.
        Returns dict with 'language' code and 'confidence' score.
        """
        if not self.client:
            return self._mock_detect(text)

        try:
            result = self.client.detect_language(text)
            return {
                'language': result.get('language', 'en'),
                'confidence': result.get('confidence', 0.0),
            }
        except Exception as e:
            logger.error('Language detection failed: %s', e)
            return self._mock_detect(text)

    def translate(self, text, target_language, source_language=None):
        """
        Translate text to the target language.
        Optionally specify source language; otherwise auto-detect.
        """
        if not self.client:
            return self._mock_translate(text, target_language, source_language)

        try:
            if source_language and source_language != 'auto':
                result = self.client.translate(
                    text,
                    target_language=target_language,
                    source_language=source_language,
                )
            else:
                result = self.client.translate(text, target_language=target_language)

            return {
                'translated_text': result.get('translatedText', text),
                'detected_source_language': result.get('detectedSourceLanguage', source_language or 'en'),
                'source_language': source_language or result.get('detectedSourceLanguage', 'en'),
            }
        except Exception as e:
            logger.error('Translation failed: %s', e)
            return self._mock_translate(text, target_language, source_language)

    def _mock_detect(self, text):
        """Fallback detection when API is unavailable (development/demo)."""
        # Simple heuristic: check for common non-Latin scripts
        if any('\u0600' <= c <= '\u06FF' for c in text):
            return {'language': 'ar', 'confidence': 0.8}
        if any('\u4e00' <= c <= '\u9fff' for c in text):
            return {'language': 'zh', 'confidence': 0.8}
        if any('\u3040' <= c <= '\u30ff' for c in text):
            return {'language': 'ja', 'confidence': 0.8}
        return {'language': 'en', 'confidence': 0.7}

    def _mock_translate(self, text, target_language, source_language=None):
        """Fallback translation prefix when API is unavailable."""
        lang_names = dict(settings.SUPPORTED_LANGUAGES)
        target_name = lang_names.get(target_language, target_language)
        return {
            'translated_text': f'[{target_name}] {text}',
            'detected_source_language': source_language or 'en',
            'source_language': source_language or 'en',
        }


# Singleton instance for reuse across requests
translation_service = TranslationService()
