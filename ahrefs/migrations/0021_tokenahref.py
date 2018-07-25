# Generated by Django 2.0.3 on 2018-07-10 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahrefs', '0020_singlebacklinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenAhref',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Token',
            },
        ),
    ]
