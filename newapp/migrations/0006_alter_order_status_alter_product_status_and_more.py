# Generated by Django 5.0 on 2024-02-03 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_rename_rent_per_day_product_rent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Status',
            field=models.CharField(choices=[('0', 'Pending'), ('1', 'Confirm')], max_length=25),
        ),
        migrations.AlterField(
            model_name='product',
            name='Status',
            field=models.CharField(choices=[('0', 'Not Available'), ('1', 'Available')], max_length=25),
        ),
        migrations.AlterField(
            model_name='user',
            name='Status',
            field=models.CharField(choices=[('0', 'Inactive'), ('1', 'Active')], max_length=25),
        ),
        migrations.CreateModel(
            name='Home_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Rent', models.CharField(max_length=20)),
                ('Product_color', models.CharField(max_length=20)),
                ('Product_size', models.CharField(max_length=20)),
                ('Product_description', models.TextField()),
                ('image', models.ImageField(upload_to='photos')),
                ('Status', models.CharField(choices=[('0', 'Not Available'), ('1', 'Available')], max_length=25)),
                ('Category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.category')),
                ('Sub_Category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.sub_cat')),
            ],
        ),
    ]
