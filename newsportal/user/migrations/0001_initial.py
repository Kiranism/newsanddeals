# Generated by Django 3.1.6 on 2021-07-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logid', models.IntegerField()),
                ('name', models.CharField(db_column='NAME', max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(db_column='phone number', max_length=15)),
                ('password', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
