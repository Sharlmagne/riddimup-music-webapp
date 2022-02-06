# Generated by Django 3.2.8 on 2021-11-10 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_alter_track_track'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='user',
        ),
        migrations.AddField(
            model_name='track',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]