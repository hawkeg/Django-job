# Generated by Django 4.0.3 on 2022-03-15 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default=1, upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
