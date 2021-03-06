# Generated by Django 4.0 on 2021-12-28 13:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pintxos', '0002_pintxovote'),
    ]

    operations = [
        migrations.AddField(
            model_name='pintxo',
            name='voted_by',
            field=models.ManyToManyField(related_name='voter', through='pintxos.PintxoVote', to=settings.AUTH_USER_MODEL),
        ),
    ]
