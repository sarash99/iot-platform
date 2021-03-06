# Generated by Django 3.2.5 on 2021-07-31 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('feed_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('field1', models.FloatField(null=True)),
                ('field2', models.FloatField(null=True)),
                ('field3', models.FloatField(null=True)),
                ('field4', models.FloatField(null=True)),
                ('field5', models.FloatField(null=True)),
                ('field6', models.FloatField(null=True)),
                ('field7', models.FloatField(null=True)),
                ('field8', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('channel_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='channel.channel')),
            ],
        ),
    ]
