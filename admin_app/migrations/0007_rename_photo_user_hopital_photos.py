# Generated by Django 3.2.8 on 2023-04-08 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0006_auto_20230302_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_hopital',
            old_name='photo',
            new_name='photos',
        ),
    ]
