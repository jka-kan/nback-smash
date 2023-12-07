# Generated by Django 3.2.12 on 2022-09-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nback_app', '0002_auto_20220911_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='colored_grid',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='distraction',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='rotate',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='sounds',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
