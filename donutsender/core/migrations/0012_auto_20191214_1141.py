# Generated by Django 2.2.7 on 2019-12-14 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20191212_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('email_is_enabled', models.BooleanField(default=True)),
                ('pop_up_is_enabled', models.BooleanField(default=True)),
                ('auto_withdraw_is_enabled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'settings',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='auto_withdraw_is_enabled',
        ),
        migrations.DeleteModel(
            name='Notifications',
        ),
        migrations.AddField(
            model_name='settings',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
