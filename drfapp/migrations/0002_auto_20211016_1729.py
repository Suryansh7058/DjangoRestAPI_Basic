# Generated by Django 3.2.8 on 2021-10-16 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
