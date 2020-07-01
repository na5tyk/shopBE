# Generated by Django 3.0.7 on 2020-07-01 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Category name')),
                ('description', models.TextField()),
                ('index', models.IntegerField(default=0, verbose_name='Index order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Product name')),
                ('description', models.TextField()),
                ('price', models.FloatField(default=0, verbose_name='Price')),
                ('amount', models.FloatField(default=0, verbose_name='Amount')),
                ('categories', models.ManyToManyField(to='product.ProductCategory')),
            ],
        ),
    ]