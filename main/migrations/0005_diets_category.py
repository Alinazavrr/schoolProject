# Generated by Django 4.2.5 on 2023-11-02 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_diets_category_remove_diets_colories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diets',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
    ]
