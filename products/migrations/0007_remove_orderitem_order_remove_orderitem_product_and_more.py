# Generated by Django 4.2.4 on 2023-09-21 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]