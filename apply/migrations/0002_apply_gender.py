# Generated by Django 3.2.2 on 2021-05-06 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='gender',
            field=models.BooleanField(default=True),
        ),
    ]
