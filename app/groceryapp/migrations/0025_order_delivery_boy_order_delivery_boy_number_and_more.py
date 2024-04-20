# Generated by Django 4.2.6 on 2024-04-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0024_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_boy',
            field=models.CharField(default='not allotted', max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_boy_number',
            field=models.IntegerField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.IntegerField(max_length=15),
        ),
    ]