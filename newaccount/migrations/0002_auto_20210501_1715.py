# Generated by Django 3.2 on 2021-05-01 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newaccount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='userStartingBalance',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newuser',
            name='userContact',
            field=models.IntegerField(max_length=15),
        ),
    ]