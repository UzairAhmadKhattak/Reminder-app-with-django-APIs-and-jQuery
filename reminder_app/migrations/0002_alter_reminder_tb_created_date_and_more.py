# Generated by Django 4.0.2 on 2022-07-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder_tb',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reminder_tb',
            name='reminder_time',
            field=models.DateTimeField(),
        ),
    ]
