# Generated by Django 3.2.5 on 2021-07-31 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('channel_name', models.CharField(max_length=100)),
                ('channel_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('field1', models.CharField(max_length=50, null=True)),
                ('field2', models.CharField(max_length=50, null=True)),
                ('field3', models.CharField(max_length=50, null=True)),
                ('field4', models.CharField(max_length=50, null=True)),
                ('field5', models.CharField(max_length=50, null=True)),
                ('field6', models.CharField(max_length=50, null=True)),
                ('field7', models.CharField(max_length=50, null=True)),
                ('field8', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
