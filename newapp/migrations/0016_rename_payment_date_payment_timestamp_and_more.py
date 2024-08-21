# Generated by Django 5.0 on 2024-03-12 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0015_remove_order_cart_id_alter_payment_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='Payment_date',
            new_name='Timestamp',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='Card_id',
        ),
        migrations.AddField(
            model_name='card',
            name='Card_Balance',
            field=models.FloatField(default=100000),
        ),
        migrations.AddField(
            model_name='payment',
            name='Payment_Method',
            field=models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='Trans_id',
            field=models.CharField(max_length=23, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='Expiry_date',
            field=models.CharField(max_length=30),
        ),
    ]
