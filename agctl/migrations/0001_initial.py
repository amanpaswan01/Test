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
                ('port', models.CharField(max_length=10)),
                ('client_channel_name', models.CharField(max_length=255)),
            ],
        ),
    ]