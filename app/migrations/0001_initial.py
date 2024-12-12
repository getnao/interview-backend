# Generated by Django 5.1.4 on 2024-12-12 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('image_url', models.CharField(max_length=2083)),
                ('description', models.TextField()),
                ('categories', models.CharField(max_length=255)),
            ],
        ),
    ]
