# Generated by Django 2.1.5 on 2020-06-11 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0009_auto_20200611_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.IntegerField(choices=[(1, 'Confirmed! Please inform manager on arrival'), (2, 'Manager will ensure that you are in the restaurant. Please wait'), (3, 'Manager has confirmed. Start Ordering now!'), (4, 'Food ordering and preparation in progress'), (5, 'Awaiting Bill Payment Confirmation'), (6, 'Bill Paid and Reservation Over'), (7, 'Feedback given')], default=1),
        ),
    ]
