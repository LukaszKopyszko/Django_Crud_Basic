# Generated by Django 2.2.12 on 2021-03-17 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('salary', models.FloatField()),
                ('gender', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
