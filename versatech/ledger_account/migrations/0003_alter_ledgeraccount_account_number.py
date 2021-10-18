# Generated by Django 3.2.8 on 2021-10-17 23:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ledger_account', '0002_alter_ledgeraccount_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledgeraccount',
            name='account_number',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
