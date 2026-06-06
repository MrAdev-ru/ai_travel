from django.db import models


class PhraseCategory(models.Model):
    """
    Travel phrasebook categories (Airport, Hotel, Restaurant, etc.).
    """

    CATEGORY_CHOICES = [
        ('airport', 'Airport'),
        ('hotel', 'Hotel'),
        ('restaurant', 'Restaurant'),
        ('taxi', 'Taxi'),
        ('shopping', 'Shopping'),
        ('emergency', 'Emergency'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon = models.CharField(
        max_length=50,
        help_text='Bootstrap Icons class name (e.g. bi-airplane)',
    )
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Phrase categories'

    def __str__(self):
        return self.name


class Phrase(models.Model):
    """
    Individual travel phrases with pre-stored translations.
    Translations stored as JSON: {"es": "...", "fr": "...", ...}
    """

    category = models.ForeignKey(
        PhraseCategory,
        on_delete=models.CASCADE,
        related_name='phrases',
    )
    source_text = models.CharField(max_length=500, help_text='English phrase')
    source_language = models.CharField(max_length=10, default='en')
    # Pre-stored translations for common languages
    translations = models.JSONField(
        default=dict,
        help_text='Language code to translated text mapping',
    )
    pronunciation = models.CharField(
        max_length=500,
        blank=True,
        help_text='Optional phonetic pronunciation guide',
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'source_text']

    def __str__(self):
        return f'{self.category.name}: {self.source_text}'

    def get_translation(self, lang_code):
        """Return translation for given language code, or source text as fallback."""
        return self.translations.get(lang_code, self.source_text)
