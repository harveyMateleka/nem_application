# Generated by Django 3.2.8 on 2023-04-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0008_hopital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_hopital',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
