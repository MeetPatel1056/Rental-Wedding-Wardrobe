# Generated by Django 5.0 on 2024-02-13 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0010_alter_complain_status_alter_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Status',
            field=models.CharField(choices=[('Confirm', 'Confirm'), ('Pending', 'Pending')], max_length=25),
        ),
        migrations.AlterField(
            model_name='complain',
            name='Status',
            field=models.CharField(choices=[('1', 'Unsolved'), ('0', 'Solved')], max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='Status',
            field=models.CharField(choices=[('1', 'Confirm'), ('0', 'Pending')], max_length=25),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Status',
            field=models.CharField(choices=[('0', 'Paid'), ('1', 'Unpaid')], max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='Status',
            field=models.CharField(choices=[('1', 'Active'), ('0', 'Inactive')], max_length=25),
        ),
    ]
