# Generated by Django 2.1.4 on 2018-12-12 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_predict', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historydata',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='predictdata',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]