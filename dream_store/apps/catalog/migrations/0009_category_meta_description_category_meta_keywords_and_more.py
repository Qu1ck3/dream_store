# Generated by Django 5.0.4 on 2024-04-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_product_meta_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Title'),
        ),
    ]
