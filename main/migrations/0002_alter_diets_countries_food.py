# Generated by Django 4.2.5 on 2023-10-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diets',
            name='countries_food',
            field=models.ManyToManyField(to='main.countryfood'),
        ),
    ]
