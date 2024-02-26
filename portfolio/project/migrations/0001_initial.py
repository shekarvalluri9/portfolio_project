# Generated by Django 5.0.1 on 2024-02-26 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(verbose_name='')),
                ('image', models.ImageField(upload_to='project_images/')),
                ('github', models.URLField(blank=True)),
                ('demo', models.URLField(blank=True)),
            ],
        ),
    ]
