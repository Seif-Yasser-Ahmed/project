# Generated by Django 4.2 on 2023-05-19 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_cartitem_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Cart',
            new_name='cart',
        ),
    ]
