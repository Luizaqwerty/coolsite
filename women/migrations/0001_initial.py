# Generated by Django 5.0 on 2023-12-19 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=99)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=18)),
                ('nationality', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='women/')),
            ],
        ),
    ]
