# Generated by Django 5.1.1 on 2024-09-30 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_inbound_inventory_outbound_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbound',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='category',
            field=models.CharField(choices=[('Electronic', 'Electronic'), ('Furniture', 'Furniture'), ('Clothing', 'Clothing')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='outbound',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]