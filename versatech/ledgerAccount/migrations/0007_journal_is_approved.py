# Generated by Django 3.2.8 on 2021-12-09 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledgerAccount', '0006_auto_20211209_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
