# Generated by Django 2.1.7 on 2019-08-06 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neuralnetwork', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadimage',
            name='height',
        ),
        migrations.RemoveField(
            model_name='uploadimage',
            name='weight',
        ),
    ]
