# Generated by Django 2.1.5 on 2019-01-16 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_news_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='employee_id',
            field=models.PositiveIntegerField(),
        ),
    ]
