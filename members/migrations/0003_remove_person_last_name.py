# Generated by Django 4.2.11 on 2024-04-26 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_person_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
    ]
