# Generated by Django 3.0.3 on 2020-03-26 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=50, verbose_name='Nick')),
                ('message', models.CharField(max_length=500, verbose_name='Message')),
            ],
        ),
    ]
