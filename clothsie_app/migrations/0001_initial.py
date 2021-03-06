# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-17 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('date_added', models.DateField()),
                ('date_purchased', models.DateField()),
                ('zipcode', models.IntegerField()),
                ('price', models.FloatField()),
                ('size', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('item_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('items_bought', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_bought', to='clothsie_app.Item')),
                ('items_selling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_selling', to='clothsie_app.Item')),
                ('items_sold', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_sold', to='clothsie_app.Item')),
            ],
        ),
    ]
