# Generated by Django 5.0.4 on 2024-04-26 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_product_meta_description_product_meta_keywords_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Keywords'),
        ),
    ]
