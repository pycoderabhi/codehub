# Generated by Django 5.0.3 on 2024-04-16 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='employe', max_length=180)),
                ('email', models.EmailField(max_length=254)),
                ('passwod', models.IntegerField(default='12345678')),
                ('dob', models.DateField()),
                ('post', models.CharField(max_length=20)),
            ],
        ),
    ]
