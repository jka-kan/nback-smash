# Generated by Django 3.2.12 on 2022-10-08 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nback_app', '0010_alter_userdata_distraction_interval'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='audio_volume',
            field=models.IntegerField(default=10),
        ),
    ]
