# Generated by Django 3.2.7 on 2021-10-10 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField(max_length=250)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
