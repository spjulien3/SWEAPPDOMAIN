# Generated by Django 4.0 on 2021-12-11 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ledgerAccount', '0011_alter_journal_journal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledgerAccount.journal'),
        ),
    ]