# Generated by Django 4.0.4 on 2022-05-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covered_business', '0004_remove_coveredbusiness_is_internal_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coveredbusiness',
            name='api_endpoint',
            field=models.URLField(blank=True, default='', max_length=127),
        ),
    ]
