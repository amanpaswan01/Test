# Generated by Django 4.2.2 on 2023-06-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_channel_name', models.CharField(max_length=255)),
                ('group', models.CharField(max_length=10)),
                ('ip_address', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
