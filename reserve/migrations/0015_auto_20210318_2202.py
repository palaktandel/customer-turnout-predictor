# Generated by Django 2.2.13 on 2021-03-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0014_auto_20210318_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='prob',
        ),
        migrations.AddField(
            model_name='pendingres',
            name='prob',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
