# Generated by Django 4.2.5 on 2023-11-02 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_diets_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diets',
            name='countries_food',
            field=models.ManyToManyField(blank=True, null=True, to='main.countryfood'),
        ),
    ]
