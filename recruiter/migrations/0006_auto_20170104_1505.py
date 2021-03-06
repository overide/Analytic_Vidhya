# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-04 15:05
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0005_auto_20161230_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='ctc',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='pg_passing_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='pg_tire1',
            field=models.CharField(blank=True, default='No', max_length=3),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='ug_course',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='ug_institute_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='ug_passing_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
