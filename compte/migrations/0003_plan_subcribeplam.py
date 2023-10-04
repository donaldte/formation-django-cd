# Generated by Django 4.2.5 on 2023-10-04 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0002_user_groups_user_user_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('metadata', models.JSONField(blank=True, default=dict, null=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubcribePlam',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('metadata', models.JSONField(blank=True, default=dict, null=True)),
                ('payment_mode', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='compte.plan')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
