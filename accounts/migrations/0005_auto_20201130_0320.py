# Generated by Django 3.1.2 on 2020-11-30 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201130_0320'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='accounts-users',
        ),
    ]
