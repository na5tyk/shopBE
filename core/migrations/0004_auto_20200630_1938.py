# Generated by Django 3.0.7 on 2020-06-30 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200630_1933'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='UserAddress',
        ),
    ]
