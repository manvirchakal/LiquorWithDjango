# Generated by Django 2.0.7 on 2022-01-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220111_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=False, upload_to=None),
            preserve_default=False,
        ),
    ]
