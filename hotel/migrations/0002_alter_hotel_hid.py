# Generated by Django 5.0.6 on 2024-06-12 17:09

import shortuuid.django_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijlmnopqrstvwxyz123', length=10, max_length=20, prefix='', unique=True),
        ),
    ]
