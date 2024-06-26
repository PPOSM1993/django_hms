# Generated by Django 5.0.6 on 2024-06-12 18:09

import django.db.models.deletion
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_alter_hotel_hid'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelFaqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.CharField(blank=True, max_length=1000, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
            options={
                'verbose_name_plural': 'Hotel FAQs',
            },
        ),
        migrations.CreateModel(
            name='HotelFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_type', models.CharField(choices=[('Bootstrap Icons', 'Bootstrap Icons'), ('Font awesome Icons', 'Font awesome Icons'), ('Box Icons', 'Box Icons'), ('Remi Icons', 'Remi Icons'), ('Flat Icons', 'Flat Icons')], max_length=100, null=True)),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
            options={
                'verbose_name_plural': 'Hotel Features',
            },
        ),
        migrations.CreateModel(
            name='HotelGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='hotel_galley')),
                ('hgid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijlmnopqrstvwxyz123', length=10, max_length=20, prefix='', unique=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
            options={
                'verbose_name_plural': 'Hotel Gallery',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('number_of_beds', models.PositiveIntegerField(default=0)),
                ('room_capacity', models.PositiveIntegerField(default=0)),
                ('rtid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijlmnopqrstvwxyz123', length=10, max_length=20, prefix='', unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
            options={
                'verbose_name_plural': 'Room Type',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=1000)),
                ('is_available', models.BooleanField(default=True)),
                ('rid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijlmnopqrstvwxyz123', length=10, max_length=20, prefix='', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.roomtype')),
            ],
            options={
                'verbose_name_plural': 'Rooms',
            },
        ),
    ]
