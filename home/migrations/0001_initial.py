# Generated by Django 4.2.5 on 2023-09-15 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField(blank=True)),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('rank', models.IntegerField()),
                ('slug', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('logo', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('comment', models.TextField()),
                ('Post', models.CharField(max_length=300)),
                ('star', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add', models.TextField()),
                ('email', models.EmailField(max_length=300)),
                ('phone', models.CharField(max_length=15)),
                ('twitter', models.URLField(blank=True, max_length=500)),
                ('facebook', models.URLField(blank=True, max_length=500)),
                ('instagram', models.URLField(blank=True, max_length=500)),
                ('linkedin', models.URLField(blank=True, max_length=500)),
                ('youtube', models.URLField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True, max_length=500)),
                ('rank', models.IntegerField()),
            ],
        ),
    ]
