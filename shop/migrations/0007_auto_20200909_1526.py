# Generated by Django 3.1 on 2020-09-09 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
    ]