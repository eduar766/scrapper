# Generated by Django 2.0.3 on 2018-06-21 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahrefs', '0014_auto_20180621_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrappertest',
            name='comentario',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='scrappertest',
            name='foro',
            field=models.BooleanField(default=False),
        ),
    ]
