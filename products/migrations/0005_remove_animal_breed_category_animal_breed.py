# Generated by Django 5.0 on 2023-12-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_animalcategory_remove_animal_breed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='breed_category',
        ),
        migrations.AddField(
            model_name='animal',
            name='breed',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
