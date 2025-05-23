# Generated by Django 5.1.7 on 2025-03-13 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='experience_level',
            field=models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.TextField(blank=True, help_text='Comma-separated list of interests (e.g., Django, React)'),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
