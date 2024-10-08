# Generated by Django 5.0 on 2024-03-12 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0017_alter_order_status_alter_payment_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='End_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Payment_mode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Start_date',
        ),
        migrations.AddField(
            model_name='order',
            name='Time_stamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='complain',
            name='Status',
            field=models.CharField(choices=[('Unsolved', 'Unsolved'), ('Solved', 'Solved')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='Status',
            field=models.CharField(choices=[('Not Available', 'Not Available'), ('Available', 'Available')], max_length=25),
        ),
    ]
