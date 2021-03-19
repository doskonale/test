# Generated by Django 3.1.7 on 2021-03-19 17:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_auto_20210316_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='Please input product name', max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(4, 'Project name should be at least 4 characters, ex. T825')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Please input product price', max_digits=10, null=True),
        ),
    ]