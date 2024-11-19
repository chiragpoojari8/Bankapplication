# Generated by Django 5.1.3 on 2024-11-18 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0011_servicerequest_loan_amount_servicerequest_loan_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='service_type',
            field=models.CharField(choices=[('Cheque Book', 'Cheque Book'), ('Credit/Debit Card', 'Credit/Debit Card'), ('Loan Inquiry', 'Loan Inquiry'), ('ATM Card Blocking/Replacement', 'ATM Card Blocking/Replacement'), ('Address Change', 'Address Change'), ('Transaction Limit', 'Transaction Limit')], max_length=50),
        ),
    ]