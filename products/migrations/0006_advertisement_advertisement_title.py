# Generated by Django 3.1.3 on 2020-12-02 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201202_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='advertisement_title',
            field=models.CharField(default='', max_length=150),
        ),
    ]
