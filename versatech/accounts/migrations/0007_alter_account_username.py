# Generated by Django 4.0 on 2021-12-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_account_password_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
