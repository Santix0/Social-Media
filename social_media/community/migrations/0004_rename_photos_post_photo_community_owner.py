# Generated by Django 4.1.4 on 2022-12-30 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0003_alter_followers_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='photos',
            new_name='photo',
        ),
        migrations.AddField(
            model_name='community',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]