# Generated by Django 3.2.9 on 2022-01-22 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0003_invoice_is_paid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ('-created_at',)},
        ),
    ]
