from django import forms
from django.conf import settings


class TranslationForm(forms.Form):
    """Form for the main translation interface."""

    source_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control translation-textarea',
            'rows': 5,
            'placeholder': 'Enter text to translate...',
            'id': 'sourceText',
        }),
        label='Text to translate',
    )
    source_language = forms.ChoiceField(
        choices=[('auto', 'Detect Language')] + list(settings.SUPPORTED_LANGUAGES),
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'sourceLanguage'}),
        initial='auto',
        label='From',
    )
    target_language = forms.ChoiceField(
        choices=settings.SUPPORTED_LANGUAGES,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'targetLanguage'}),
        initial='es',
        label='To',
    )
