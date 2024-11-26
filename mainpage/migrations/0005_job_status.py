# Generated by Django 3.0.8 on 2020-08-25 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_remove_job_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('yes', 'Yes'), ('noreply', 'No Reply'), ('rejected', 'Rejected')], default='noreply', max_length=50),
        ),
    ]
