# Generated by Django 4.0.1 on 2022-04-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pickup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('pickupAddress', models.CharField(max_length=350)),
                ('pickupPersonName', models.CharField(max_length=100)),
                ('pickupPersonNumber', models.IntegerField()),
                ('deliveryAddress', models.CharField(max_length=350)),
                ('pickupRequestByUserId', models.IntegerField(default='null', editable=False)),
                ('pickupDeliveryPersonId', models.IntegerField(default='null', editable=False)),
                ('timeLimit', models.IntegerField()),
                ('status', models.BooleanField(default=0)),
            ],
        ),
    ]
