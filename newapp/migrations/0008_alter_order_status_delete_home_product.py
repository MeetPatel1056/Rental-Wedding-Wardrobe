# Generated by Django 5.0 on 2024-02-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_alter_payment_status_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Status',
            field=models.CharField(choices=[('1', 'Confirm'), ('0', 'Pending')], max_length=25),
        ),
        migrations.DeleteModel(
            name='Home_Product',
        ),
    ]
