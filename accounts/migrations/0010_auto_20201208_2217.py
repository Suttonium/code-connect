# Generated by Django 3.1.2 on 2020-12-08 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Non Binary'), ('X', 'Prefer Not To Say')], default='X', max_length=1),
        ),
    ]
