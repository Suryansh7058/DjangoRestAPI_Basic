# Generated by Django 3.2.8 on 2021-10-16 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfapp', '0002_auto_20211016_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]