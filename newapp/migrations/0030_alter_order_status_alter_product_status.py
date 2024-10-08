# Generated by Django 5.0.4 on 2024-06-27 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0029_alter_order_status_alter_product_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirm', 'Confirm'), ('Cancelled', 'Cancelled')], max_length=25),
        ),
        migrations.AlterField(
            model_name='product',
            name='Status',
            field=models.CharField(choices=[('Not Available', 'Not Available'), ('Available', 'Available')], max_length=25),
        ),
    ]
