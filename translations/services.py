"""
Deep Translator service wrapper.
Handles translation and fallback behavior using deep-translator.
"""
import logging

from django.conf import settings

logger = logging.getLogger(__name__)


class TranslationService:
    """Service class for translation operations using deep-translator."""

    def is_available(self):
        """Check if the deep-translator package is importable."""
        try:
            from deep_translator import GoogleTranslator  # noqa: F401
            return True
        except Exception as e:
            logger.warning('Deep Translator unavailable: %s', e)
            return False

    def detect_language(self, text):
        """Detect the language of the given text using script heuristics."""
        return self._detect_language(text)

    def translate(self, text, target_language, source_language=None):
        """
        Translate text to the target language.
        Optionally specify source language; otherwise auto-detect.
        """
        try:
            from deep_translator import GoogleTranslator

            translator_source = (
                source_language if source_language and source_language != 'auto' else 'auto'
            )
            translated_text = GoogleTranslator(
                source=translator_source,
                target=target_language,
            ).translate(text)

            return {
                'translated_text': translated_text,
                'detected_source_language': translator_source,
                'source_language': translator_source,
            }
        except Exception as e:
            logger.error('Translation failed: %s', e)
            return self._mock_translate(text, target_language, source_language)

    def _detect_language(self, text):
        """Fallback detection using simple script heuristics."""
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
