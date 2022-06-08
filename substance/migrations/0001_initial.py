# Generated by Django 4.0.3 on 2022-04-11 18:17

from django.db import migrations, models
import django.db.models.deletion
import litsource.models
import wagtail.blocks
import wagtail.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Substance',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('soilprops', wagtail.fields.StreamField([('PDKp', wagtail.blocks.StructBlock([('value', wagtail.blocks.FloatBlock(label='Предельно допустимая концентрация в почве (ПДКп) [мг/кг]', min_value=0, required=True)), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))])), ('ODKp', wagtail.blocks.StructBlock([('value', wagtail.blocks.FloatBlock(label='Ориентировочно допустимые концентрации в почве (ОДК) [мг/кг]', min_value=0, required=True)), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))])), ('SclsSoil', wagtail.blocks.StructBlock([('value', wagtail.blocks.ChoiceBlock(choices=[('1', 'I класс'), ('2', 'II класс'), ('3', 'III класс'), ('4', 'не установлен')], label='Класс опасности в почве')), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))]))])),
                ('dwprops', wagtail.fields.StreamField([('SclsDWater', wagtail.blocks.StructBlock([('value', wagtail.blocks.ChoiceBlock(choices=[('1', 'I класс'), ('2', 'II класс'), ('3', 'III класс'), ('4', 'IV класс')], label='Класс опасности в питьевой воде')), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))])), ('PDKw', wagtail.blocks.StructBlock([('value', wagtail.blocks.FloatBlock(label='Предельно допустимая концентрация в питьевой воде (ПДКв) [мг/л]', min_value=0, required=True)), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))])), ('oduw', wagtail.blocks.StructBlock([('value', wagtail.blocks.FloatBlock(label='Ориентировочные допустимые уровни в питьевой воде (ОДУ) [мг/л]', min_value=0, required=True)), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))])), ('obuvw', wagtail.blocks.StructBlock([('value', wagtail.blocks.FloatBlock(label='Ориентировочно безопасные уровни воздействия в питьевой воде (ОБУВ) [мг/л]', min_value=0, required=True)), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))]))])),
                ('fwprops', wagtail.fields.StreamField([('SclsFWater', wagtail.blocks.StructBlock([('value', wagtail.blocks.ChoiceBlock(choices=[('1', 'I класс'), ('2', 'II класс'), ('3', 'III класс'), ('4', 'IV класс')], label='Класс опасности в воде рыбохозяйственного значения')), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))])), ('PDKfw', wagtail.blocks.StructBlock([('value', wagtail.blocks.FloatBlock(label='Предельно допустимая концентрация в воде рыбохозяйственного значения (ПДКрх) [мг/л]', min_value=0, required=True)), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))])), ('obuvfw', wagtail.blocks.StructBlock([('value', wagtail.blocks.FloatBlock(label='Ориентировочно безопасные уровни воздействия в воде рыбохозяйственного значения (ОБУВ) [мг/л]', min_value=0, required=True)), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))]))])),
                ('airprops', wagtail.fields.StreamField([('SclsAir', wagtail.blocks.StructBlock([('value', wagtail.blocks.ChoiceBlock(choices=[('1', 'I класс'), ('2', 'II класс'), ('3', 'III класс'), ('4', 'IV класс')], label='Класс опасности в воздухе')), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))])), ('PDKss', wagtail.blocks.StructBlock([('value', wagtail.blocks.FloatBlock(label='Предельно допустимая концентрация в воздухе средне-суточное зоны (ПДКсс) [мг/м<sup>3</sup>]', min_value=0, required=True)), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))])), ('PDKmr', wagtail.blocks.StructBlock([('value', wagtail.blocks.FloatBlock(label='Предельно допустимая концентрация в воздухе максимальная разовая (ПДКмр) [мг/м<sup>3</sup>]', min_value=0, required=True)), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))])), ('obuvair', wagtail.blocks.StructBlock([('value', wagtail.blocks.FloatBlock(label='Ориентировочно безопасные уровни воздействия в воздухе [мг/м<sup>3</sup>]', min_value=0, required=True)), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))]))])),
                ('ecoprops', wagtail.fields.StreamField([('presistancy', wagtail.blocks.StructBlock([('value', wagtail.blocks.ChoiceBlock(choices=[('1', 'Образование более токсичных продуктов, в т.ч. обладающих отдаленными эффектами или новыми свойствами'), ('2', 'Образование продуктов с более выраженным влиянием других критериев опасности'), ('3', 'Образование продуктов, токсичность которых близка к токсичности исходного вещества'), ('4', 'Образование менее токсичных продуктов')], label='Персистентность')), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))])), ('bioaccum', wagtail.blocks.StructBlock([('value', wagtail.blocks.ChoiceBlock(choices=[('1', 'Выраженное накопление во всех звеньях'), ('2', 'Накопление в нескольких звеньях'), ('3', 'Накопление в одном из звеньев'), ('4', 'Накопление отсутствует')], label='Биоаккумуляция')), ('source', wagtail.snippets.blocks.SnippetChooserBlock(litsource.models.LitSource, label='Источник литературы для значения', required=True))]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
