# Generated by Django 2.2.13 on 2021-03-18 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0015_auto_20210318_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='phase',
            field=models.IntegerField(default=2, max_length='2'),
            preserve_default=False,
        ),
    ]
