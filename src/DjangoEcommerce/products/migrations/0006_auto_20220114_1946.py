# Generated by Django 2.0.7 on 2022-01-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/images/'),
        ),
    ]
