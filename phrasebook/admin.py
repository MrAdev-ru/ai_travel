from django.contrib import admin
from .models import PhraseCategory, Phrase


class PhraseInline(admin.TabularInline):
    model = Phrase
    extra = 1
    fields = ('source_text', 'translations', 'pronunciation', 'order')


@admin.register(PhraseCategory)
class PhraseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'icon', 'order')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [PhraseInline]


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ('source_text', 'category', 'order')
    list_filter = ('category',)
    search_fields = ('source_text',)
