# Generated by Django 5.0 on 2024-02-06 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0008_alter_order_status_delete_home_product'),
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
            field=models.CharField(choices=[('1', 'Available'), ('0', 'Not Available')], max_length=25),
        ),
        migrations.AlterField(
            model_name='user',
            name='Status',
            field=models.CharField(choices=[('0', 'Inactive'), ('1', 'Active')], max_length=25),
        ),
    ]
