# Generated by Django 2.1.5 on 2019-01-16 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='employee_id',
            field=models.PositiveIntegerField(default=-1),
        ),
    ]
