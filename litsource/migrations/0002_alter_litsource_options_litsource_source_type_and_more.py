# Generated by Django 4.0.3 on 2022-04-10 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litsource', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='litsource',
            options={'verbose_name': 'Источник литературы', 'verbose_name_plural': 'Источники литературы'},
        ),
        migrations.AddField(
            model_name='litsource',
            name='source_type',
            field=models.CharField(choices=[('prikaz', 'Приказ'), ('gost', 'ГОСТ'), ('art', 'Статья'), ('gn', 'Гигиенические нормативы'), ('art', 'Статья'), ('sanpin', 'Санитарные (санитарно-эпидемиологические) правила и нормы')], default='art', max_length=10),
        ),
        migrations.AddField(
            model_name='litsource',
            name='source_url',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Url cсылка на источник (при наличии)'),
        ),
        migrations.AlterField(
            model_name='litsource',
            name='name',
            field=models.CharField(help_text='Укажите название источника (например Приказ Минприроды N 536)', max_length=200, unique=True, verbose_name='Название источника'),
        ),
    ]
