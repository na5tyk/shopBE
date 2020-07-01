# Generated by Django 3.0.7 on 2020-06-30 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=1, max_length=16, verbose_name='Phone'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last name')),
                ('street', models.CharField(max_length=300, verbose_name='street')),
                ('number', models.CharField(max_length=10, verbose_name='number')),
                ('premise_number', models.CharField(max_length=10, verbose_name='premise_number')),
                ('zip_code', models.CharField(max_length=16, verbose_name='Zip code')),
                ('city', models.CharField(max_length=200, verbose_name='City')),
                ('phone', models.CharField(max_length=16, verbose_name='Phone')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]