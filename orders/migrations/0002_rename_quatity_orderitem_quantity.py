# Generated by Django 4.1.7 on 2023-02-28 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='quatity',
            new_name='quantity',
        ),
    ]
