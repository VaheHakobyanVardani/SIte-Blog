# Generated by Django 3.0.5 on 2021-02-06 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='players_name',
            new_name='name',
        ),
    ]
