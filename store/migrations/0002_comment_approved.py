# Generated by Django 4.2 on 2024-02-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
    ]