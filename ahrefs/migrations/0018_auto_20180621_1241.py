# Generated by Django 2.0.3 on 2018-06-21 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahrefs', '0017_auto_20180621_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='csv_import',
            name='foro',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='csv_import',
            name='nofollow',
            field=models.BooleanField(default=False),
        ),
    ]
