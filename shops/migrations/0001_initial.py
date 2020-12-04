# Generated by Django 3.1.3 on 2020-11-29 07:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('location', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
