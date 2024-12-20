# Generated by Django 5.1.2 on 2024-11-23 03:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mr', '0002_accessories'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_name', models.CharField(max_length=255)),
                ('active_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='LineHandover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=255, null=True)),
                ('input_qty', models.IntegerField(default=0)),
                ('handover_qty', models.IntegerField(default=0)),
                ('input_date', models.DateField()),
                ('handover_date', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('style_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr.style')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.linename')),
            ],
        ),
        migrations.CreateModel(
            name='LineSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=255, null=True)),
                ('target_qty', models.IntegerField(default=0)),
                ('total_qty', models.IntegerField(default=0)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('complete_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.linename')),
                ('style_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr.style')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('note', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.lineschedule')),
            ],
        ),
    ]
