# Generated by Django 5.1.2 on 2024-12-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0005_lineuser_linename_adminuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineinputacc',
            name='issue_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]