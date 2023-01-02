# Generated by Django 4.1.4 on 2023-01-01 08:23

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_alter_photo_reference_to_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_books',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Favorite books'),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_movies',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Favorite movies'),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_music',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Favorite music'),
        ),
        migrations.AddField(
            model_name='user',
            name='hobbies',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Hobbies'),
        ),
        migrations.AddField(
            model_name='user',
            name='political_view',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Political views'),
        ),
        migrations.AddField(
            model_name='user',
            name='relationship',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('In love', 'In love'), ('In relationship', 'In relationship'), ('Married', 'Married'), ('Engaged', 'Engaged'), ('Actively searching', 'Actively searching')], max_length=50, null=True, verbose_name='Relationship'),
        ),
        migrations.AddField(
            model_name='user',
            name='religion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Religion'),
        ),
        migrations.AddField(
            model_name='user',
            name='town_of_living',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Town of living'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
    ]
