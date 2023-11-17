# Generated by Django 4.2 on 2023-06-14 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CatName', models.CharField(blank=True, max_length=20, null=True)),
                ('Description', models.CharField(blank=True, max_length=200, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='CatImages')),
            ],
        ),
    ]
