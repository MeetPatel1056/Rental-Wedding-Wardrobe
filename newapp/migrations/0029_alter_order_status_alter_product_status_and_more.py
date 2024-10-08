# Generated by Django 5.0 on 2024-04-25 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0028_feedback_product_id_alter_complain_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Pending', 'Pending'), ('Confirm', 'Confirm')], max_length=25),
        ),
        migrations.AlterField(
            model_name='product',
            name='Status',
            field=models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], max_length=25),
        ),
        migrations.AlterField(
            model_name='user',
            name='Status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=25),
        ),
        migrations.DeleteModel(
            name='Complain',
        ),
    ]
