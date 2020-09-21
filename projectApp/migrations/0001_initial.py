# Generated by Django 3.1.1 on 2020-09-21 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShadowAmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'shadowamps',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('STR', models.IntegerField()),
                ('AGL', models.IntegerField()),
                ('WILL', models.IntegerField()),
                ('LOG', models.IntegerField()),
                ('CHA', models.IntegerField()),
                ('EDG', models.IntegerField()),
                ('ShadowAmp', models.ManyToManyField(to='projectApp.ShadowAmp')),
            ],
            options={
                'verbose_name_plural': 'characters',
            },
        ),
    ]