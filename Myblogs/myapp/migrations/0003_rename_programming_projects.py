# Generated by Django 4.2.10 on 2024-02-12 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_programming_type_of_project'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Programming',
            new_name='Projects',
        ),
    ]
