# Generated by Django 5.0.3 on 2024-04-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addaccount', '0004_accounts_dob_accounts_email_accounts_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='dob',
            field=models.DateField(),
        ),
    ]
