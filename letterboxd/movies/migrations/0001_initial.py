# Generated by Django 5.0.1 on 2024-01-03 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageUrl', models.URLField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('age', models.PositiveIntegerField()),
                ('director', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
            ],
        ),
    ]
