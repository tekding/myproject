# Generated by Django 4.1 on 2022-08-26 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_alter_standard_stdnum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standard',
            name='stdnum',
            field=models.IntegerField(),
        ),
    ]
