# Generated by Django 5.0.1 on 2024-02-03 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_alter_order_status_alter_product_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Status',
            field=models.CharField(choices=[('1', 'Available'), ('0', 'Not Available')], max_length=25),
        ),
        migrations.CreateModel(
            name='Sub_cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sub_catName', models.CharField(max_length=70)),
                ('Category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='Sub_cat_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='newapp.sub_cat'),
            preserve_default=False,
        ),
    ]
