# Generated by Django 5.0.3 on 2024-04-16 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addaccount', '0002_alter_accounts_name_alter_accounts_passwod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='email',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='name',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='passwod',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='post',
        ),
    ]
