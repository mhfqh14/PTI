# Generated by Django 3.2.9 on 2022-04-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('nama', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('alamat', models.TextField()),
                ('nomor_handphone', models.CharField(max_length=16)),
            ],
        ),
    ]
