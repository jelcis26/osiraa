# Generated by Django 3.2.12 on 2023-04-04 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drp_pip', '0003_datarightsrequest_datarightsstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='datarightsrequest',
            name='aa_id',
            field=models.CharField(blank=True, default='', max_length=63),
        ),
        migrations.AddField(
            model_name='datarightsstatus',
            name='aa_id',
            field=models.CharField(blank=True, default='', max_length=63),
        ),
    ]
