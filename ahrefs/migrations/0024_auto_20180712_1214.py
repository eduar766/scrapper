# Generated by Django 2.0.3 on 2018-07-12 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahrefs', '0023_auto_20180712_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv_import',
            name='language',
            field=models.CharField(blank=True, choices=[('Español', 'Español'), ('Ingles', 'Ingles'), ('it', 'Italiano'), ('Ruso', 'Ruso'), ('ja', 'Japones')], max_length=200, null=True),
        ),
    ]
