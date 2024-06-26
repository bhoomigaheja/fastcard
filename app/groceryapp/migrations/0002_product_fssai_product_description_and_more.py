# Generated by Django 4.2.6 on 2024-03-17 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='FSSAI',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='Not provided'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_features',
            field=models.TextField(default='Not provided'),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacture_detail',
            field=models.TextField(default='Not provided'),
        ),
        migrations.AddField(
            model_name='product',
            name='q1',
            field=models.CharField(default='Default value for q1', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='q2',
            field=models.CharField(default='Default value for q1', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='q3',
            field=models.CharField(default='Default value for q1', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.CharField(default='Default value for q1', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='shelflife',
            field=models.CharField(default='Default value for q1', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='product2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='eshop/static/images')),
                ('name', models.CharField(default='Default value for q1', max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('image2', models.ImageField(upload_to='eshop/static/images')),
                ('q1', models.CharField(default='Default value for q1', max_length=255)),
                ('description_features', models.TextField(default='Not provided')),
                ('shelflife', models.CharField(default='Default value for q1', max_length=255)),
                ('manufacture_detail', models.TextField(default='Not provided')),
                ('FSSAI', models.IntegerField(default=0)),
                ('description', models.TextField(default='Not provided')),
                ('seller', models.CharField(default='Default value for q1', max_length=255)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='groceryapp.category')),
            ],
        ),
    ]
