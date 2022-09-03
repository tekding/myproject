# Generated by Django 4.1 on 2022-08-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_company_standard_to_company_standard_companies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company',
        ),
        migrations.AddField(
            model_name='company',
            name='company_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
