# Generated by Django 2.2.24 on 2021-08-10 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_api_key', '0004_prefix_hashed_key'),
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='api_key',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='rest_framework_api_key.APIKey'),
        ),
    ]
