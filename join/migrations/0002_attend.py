# Generated by Django 2.2.4 on 2019-09-05 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nid', models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]
