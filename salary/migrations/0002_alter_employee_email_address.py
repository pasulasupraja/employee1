# Generated by Django 4.2.11 on 2024-04-25 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email_address',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
