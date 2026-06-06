# Generated migration for phrasebook app

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='PhraseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('icon', models.CharField(help_text='Bootstrap Icons class name (e.g. bi-airplane)', max_length=50)),
                ('description', models.TextField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Phrase categories',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_text', models.CharField(help_text='English phrase', max_length=500)),
                ('source_language', models.CharField(default='en', max_length=10)),
                ('translations', models.JSONField(default=dict, help_text='Language code to translated text mapping')),
                ('pronunciation', models.CharField(blank=True, help_text='Optional phonetic pronunciation guide', max_length=500)),
                ('order', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phrases', to='phrasebook.phrasecategory')),
            ],
            options={
                'ordering': ['category', 'order', 'source_text'],
            },
        ),
    ]
