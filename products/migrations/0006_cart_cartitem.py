# Generated by Django 4.2 on 2023-05-13 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_reguser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('Cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitems', to='products.cargo')),
                ('Cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitems', to='products.cart')),
                ('Hoodie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitems', to='products.hoodie')),
                ('Jacket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitems', to='products.jacket')),
                ('Jean', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitems', to='products.jean')),
                ('Oversize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitems', to='products.oversize')),
            ],
        ),
    ]
