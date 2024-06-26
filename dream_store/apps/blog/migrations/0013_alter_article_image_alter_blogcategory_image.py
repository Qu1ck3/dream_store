# Generated by Django 5.0.4 on 2024-04-16 17:08

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='blog/article/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='blog/category/', verbose_name='Изображение'),
        ),
    ]
