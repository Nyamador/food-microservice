# Generated by Django 3.1.3 on 2020-12-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Restaurant Name')),
                ('description', models.CharField(max_length=2000, verbose_name='Description')),
                ('map_url', models.URLField(max_length=2000, verbose_name='Google Map Url')),
                ('country', models.CharField(max_length=200, verbose_name='Country')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Date Added')),
            ],
        ),
    ]
