# Generated by Django 4.1.2 on 2022-11-01 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_rename_timestamp_purchases_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciperequirement',
            name='ingredient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.ingredient', verbose_name='ingredients'),
        ),
    ]
