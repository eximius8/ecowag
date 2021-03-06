# Generated by Django 4.0.5 on 2022-06-12 23:26

from django.db import migrations, models
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LitSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название источника (например Приказ Минприроды N 536)', max_length=200, unique=True, verbose_name='Название источника')),
                ('source_type', models.CharField(choices=[('prikaz', 'Приказ'), ('gost', 'ГОСТ'), ('art', 'Статья'), ('gn', 'Гигиенические нормативы'), ('art', 'Статья'), ('sanpin', 'Санитарные (санитарно-эпидемиологические) правила и нормы')], default='art', max_length=10)),
                ('source_url', models.URLField(blank=True, max_length=500, null=True, verbose_name='Url cсылка на источник (при наличии)')),
            ],
            options={
                'verbose_name': 'Источник литературы',
                'verbose_name_plural': 'Источники литературы',
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
    ]
