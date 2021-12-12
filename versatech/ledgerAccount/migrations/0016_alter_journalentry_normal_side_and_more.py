# Generated by Django 4.0 on 2021-12-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledgerAccount', '0015_remove_ledgeraccount_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='normal_side',
            field=models.CharField(choices=[('RIGHT', 'RIGHT'), ('LEFT', 'LEFT'), ('BALANCED', 'BALANCED')], max_length=10),
        ),
        migrations.AlterField(
            model_name='ledgeraccount',
            name='account_subcategory',
            field=models.CharField(blank=True, choices=[('CURRRENT', 'CURRRENT'), ('FIXED', 'FIXED'), ('LONG TERM', 'LONG TERM'), ('ACCOUNTS RECIEVABLE', 'ACCOUNTS RECIEVABLE'), ('NOTES PAYABLE', 'NOTES PAYABLE'), ('ACCRUED', 'ACCRUED'), ('DEFFERED REVENUE', 'DEFFERED REVENUE'), ('COMMON STOCK', 'COMMON STOCK'), ('PREFERRED STOCK', 'PREFERRED STOCK'), ('RETAINED EARNINGS', 'RETAINED EARNINGS'), ('DIVIDENDS', 'DIVIDENDS'), ('TREASURY STOCK', 'TREASURY STOCK')], max_length=100),
        ),
        migrations.AlterField(
            model_name='ledgeraccount',
            name='normal_side',
            field=models.CharField(blank=True, choices=[('RIGHT', 'RIGHT'), ('LEFT', 'LEFT'), ('BALANCED', 'BALANCED')], max_length=10),
        ),
    ]
