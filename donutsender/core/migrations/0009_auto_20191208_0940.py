# Generated by Django 2.2.7 on 2019-12-08 09:40

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_payment_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='money',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.1000000000000000055511151231257827021181583404541015625'), max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.1000000000000000055511151231257827021181583404541015625'))]),
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('money', models.DecimalField(decimal_places=2, default=Decimal('5'), max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('5'))])),
                ('method', models.CharField(default='card', max_length=20)),
                ('additional_info', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='withdrawals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
