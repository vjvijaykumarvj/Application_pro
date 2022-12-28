# Generated by Django 4.1.4 on 2022-12-26 05:10

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('address', models.TextField()),
                ('photo', models.ImageField(upload_to='media')),
                ('pincode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Please Enter valid Pincode', regex='[0-9]{6}')])),
                ('mobile', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Please Enter valid Phone Number', regex='[0-9]{10}')])),
                ('pancard', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Please enter a valid  Pan number', regex='[A-Z]{5}[0-9]{4}[A-Z]{1}')])),
            ],
        ),
    ]