# Generated by Django 4.2.6 on 2024-04-09 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0017_rename_landmark_order_landmark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='landmark',
            new_name='Landmark',
        ),
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.ImageField(default='img/category-1.jpg', upload_to='static/img/'),
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='groceryapp.product2'),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.CharField(default='a', max_length=5),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
