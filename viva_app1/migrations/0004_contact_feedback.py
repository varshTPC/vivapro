# Generated by Django 4.0.4 on 2022-04-17 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viva_app1', '0003_remove_contact_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='feedback',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
