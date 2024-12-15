# Generated by Django 5.1.2 on 2024-12-08 07:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mr', '0002_accessories'),
        ('production', '0006_lineinputacc_issue_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LineInputFabric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=255, null=True)),
                ('request_qty', models.IntegerField(default=0)),
                ('input_qty', models.IntegerField(default=0)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('approved', models.IntegerField(default=1)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.linename')),
                ('request_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('style_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr.style')),
            ],
        ),
    ]