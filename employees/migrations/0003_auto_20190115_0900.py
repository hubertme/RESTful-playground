# Generated by Django 2.1.5 on 2019-01-15 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20190115_0723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='lastName',
            new_name='last_name',
        ),
    ]