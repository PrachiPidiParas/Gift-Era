# Generated by Django 4.2.4 on 2024-04-14 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftgallery', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/products/'),
        ),
    ]
