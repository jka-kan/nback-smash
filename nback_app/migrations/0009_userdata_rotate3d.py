# Generated by Django 3.2.12 on 2022-10-03 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nback_app', '0008_auto_20220929_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='rotate3d',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
