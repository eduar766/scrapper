# Generated by Django 2.0.3 on 2018-07-12 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahrefs', '0026_auto_20180712_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv_import',
            name='language',
            field=models.CharField(blank=True, choices=[('es', 'Español'), ('en', 'Ingles'), ('it', 'Italiano'), ('ru', 'Ruso'), ('ja', 'Japones'), ('ru', 'Rumano'), ('nl', 'Holandés'), ('ar', 'Armenio'), ('fr', 'Francés'), ('de', 'Aleman'), ('pl', 'Polaco'), ('tw', 'Taiwanes'), ('kr', 'Koreano'), ('pt', 'Portugues')], max_length=200, null=True),
        ),
    ]
