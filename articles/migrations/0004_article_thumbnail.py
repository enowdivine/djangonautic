# Generated by Django 2.2.12 on 2023-05-31 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_article_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
