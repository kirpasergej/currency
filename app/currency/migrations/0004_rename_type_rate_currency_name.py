# Generated by Django 3.2.4 on 2021-06-11 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='type',
            new_name='currency_name',
        ),
    ]