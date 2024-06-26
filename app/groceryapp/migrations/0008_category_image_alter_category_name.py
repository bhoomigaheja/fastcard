# Generated by Django 4.2.6 on 2024-03-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0007_alter_product_image_alter_product2_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='img/logo.png', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='Default value for q1', max_length=255),
        ),
    ]
