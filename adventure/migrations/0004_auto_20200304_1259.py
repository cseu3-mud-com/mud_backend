# Generated by Django 3.0.3 on 2020-03-04 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0003_auto_20200303_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='x',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='room',
            name='y',
            field=models.IntegerField(default=None),
        ),
    ]