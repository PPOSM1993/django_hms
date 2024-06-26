# Generated by Django 5.0.6 on 2024-06-12 19:05

import django.db.models.deletion
import shortuuid.django_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_delete_booking'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('Processing', 'Processing'), ('Cancelled', 'Cancelled'), ('Initiated', 'Initiated'), ('Failed', 'Failed'), ('Refunding', 'Refunding'), ('Refunded', 'Refunded'), ('Unpaid', 'Unpaid'), ('Expired', 'Expired')], max_length=100)),
                ('full_name', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=1000)),
                ('phone', models.CharField(max_length=1000)),
                ('before_discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('saved', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('total_days', models.PositiveIntegerField(default=0)),
                ('num_adults', models.PositiveIntegerField(default=1)),
                ('num_children', models.PositiveIntegerField(default=1)),
                ('check_in', models.BooleanField(default=False)),
                ('check_out', models.BooleanField(default=False)),
                ('is_activate', models.BooleanField(default=False)),
                ('check_in_tracker', models.BooleanField(default=False)),
                ('check_out_tracker', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('stripe_payment_intent', models.CharField(blank=True, max_length=1000, null=True)),
                ('success_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('booking_id', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijlmnopqrstvwxyz123', length=10, max_length=20, prefix='', unique=True)),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.hotel')),
                ('room', models.ManyToManyField(to='hotel.room')),
                ('room_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.roomtype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess_out', models.DateTimeField()),
                ('guess_in', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.booking')),
            ],
        ),
        migrations.CreateModel(
            name='StaffOnDuty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.booking')),
            ],
        ),
    ]
