# Generated by Django 4.2 on 2024-02-28 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0003_alter_basketitem_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('amount', models.PositiveIntegerField(verbose_name='Amount')),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='pending', max_length=20, verbose_name='Payment Status')),
                ('payment_date', models.DateTimeField(blank=True, null=True, verbose_name='Payment Date')),
                ('payment_method', models.CharField(blank=True, max_length=50, null=True, verbose_name='Payment Method')),
                ('basket', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='cart.shoppingbasket', verbose_name='Basket')),
            ],
        ),
    ]