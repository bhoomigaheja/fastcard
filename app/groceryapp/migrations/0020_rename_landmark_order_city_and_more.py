# Generated by Django 4.2.6 on 2024-04-12 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groceryapp', '0019_alter_order_price_alter_order_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Landmark',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='order_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='FlatNumber',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_boy_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_time',
        ),
        migrations.RemoveField(
            model_name='order',
            name='image',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default='a', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='landmark',
            field=models.CharField(default='a', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default='a', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default=1, max_length=15),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='groceryapp.product2'),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='a', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='a', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.CharField(default='a', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]