# Generated by Django 2.2.12 on 2023-05-31 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='thumbnail',
        ),
    ]
