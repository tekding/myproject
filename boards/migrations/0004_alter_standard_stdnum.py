# Generated by Django 4.1 on 2022-08-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_alter_standard_stdnum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standard',
            name='stdnum',
            field=models.CharField(max_length=10),
        ),
    ]