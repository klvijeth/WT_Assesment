# Generated by Django 3.0.4 on 2020-05-24 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidcases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]