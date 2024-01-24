# Generated by Django 5.0 on 2024-01-24 06:10

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='women',
            options={'verbose_name': 'Women', 'verbose_name_plural': 'Women'},
        ),
        migrations.AddField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='women',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2024, 1, 24, 6, 10, 51, 674327, tzinfo=datetime.timezone.utc), max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='women',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='women',
            name='nationality',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='women',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='women.category'),
        ),
    ]
