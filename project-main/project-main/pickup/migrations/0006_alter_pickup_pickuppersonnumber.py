# Generated by Django 4.0.1 on 2022-04-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickup', '0005_alter_pickup_pickupdeliverypersonid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickup',
            name='pickupPersonNumber',
            field=models.CharField(max_length=15),
        ),
    ]
