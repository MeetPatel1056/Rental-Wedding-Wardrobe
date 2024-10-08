# Generated by Django 5.0 on 2024-03-12 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0018_remove_order_address_remove_order_end_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Total',
            new_name='Price',
        ),
        migrations.AlterField(
            model_name='complain',
            name='Status',
            field=models.CharField(choices=[('Solved', 'Solved'), ('Unsolved', 'Unsolved')], max_length=20),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Status',
            field=models.CharField(choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='Status',
            field=models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], max_length=25),
        ),
    ]
