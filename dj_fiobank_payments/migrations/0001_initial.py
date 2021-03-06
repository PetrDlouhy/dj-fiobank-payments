# Generated by Django 2.0.13 on 2019-05-21 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FioPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ident', models.CharField(blank=True, help_text='Payment identificator, usually generated by the bank', max_length=255, unique=True, verbose_name='Identificator')),
                ('symvar', models.CharField(blank=True, help_text='Variable symbol of the transaction', max_length=255, null=True, verbose_name='Variable symbol')),
                ('symcon', models.CharField(blank=True, help_text='Constant symbol of the transaction', max_length=255, null=True, verbose_name='Constant symbol')),
                ('symspc', models.CharField(blank=True, help_text='Specific symbol of the transaction', max_length=255, null=True, verbose_name='Specific symbol')),
                ('amount', models.CharField(help_text='Amount of money received in this payment in CZK', max_length=255, verbose_name='Amount received')),
                ('sender', models.CharField(blank=True, default='unknown', help_text='Account number of person sending this payment', max_length=255, null=True, verbose_name='Sender')),
                ('bank', models.CharField(blank=True, default='unknown', help_text='Bank sending this payment', max_length=255, null=True, verbose_name='Bank')),
                ('currency', models.CharField(blank=True, default='unknown', help_text='Currency of the payment', max_length=255, null=True, verbose_name='Currency')),
                ('received_at', models.DateTimeField(blank=True, help_text='When was the payment received by our bank', null=True, verbose_name='Date Time received')),
                ('message', models.TextField(blank=True, max_length=255, null=True, verbose_name='Message')),
                ('status', models.CharField(choices=[('in_progress', 'In progress'), ('paid', 'Paid'), ('cancelled', 'Cancelled')], default='in_progress', max_length=255)),
                ('user_identification', models.CharField(blank=True, help_text='User identification given by the bank', max_length=255, null=True, verbose_name='User identification')),
                ('order', models.ForeignKey(settings.FIOBANK_PAYMENTS_ORDER_MODEL, blank=True, help_text='Which order is this payment related to?', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fio_payments', verbose_name='Purchase order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
