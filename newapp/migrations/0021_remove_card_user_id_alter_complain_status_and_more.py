# Generated by Django 5.0 on 2024-03-14 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0020_order_from_date_order_to_date_alter_complain_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='User_id',
        ),
        migrations.AlterField(
            model_name='complain',
            name='Status',
            field=models.CharField(choices=[('Solved', 'Solved'), ('Unsolved', 'Unsolved')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='Status',
            field=models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], max_length=25),
        ),
        migrations.AlterField(
            model_name='user',
            name='Status',
            field=models.CharField(choices=[('Inactive', 'Inactive'), ('Active', 'Active')], max_length=25),
        ),
    ]
