# Generated by Django 4.2 on 2024-02-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_media_file_alter_product_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(upload_to='media/store/media', verbose_name='File'),
        ),
    ]
