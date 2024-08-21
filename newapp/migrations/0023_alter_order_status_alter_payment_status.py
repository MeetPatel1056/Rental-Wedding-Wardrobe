# Generated by Django 5.0 on 2024-03-14 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0022_alter_complain_status_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirm', 'Confirm')], max_length=25),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Status',
            field=models.CharField(choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], max_length=20),
        ),
    ]
