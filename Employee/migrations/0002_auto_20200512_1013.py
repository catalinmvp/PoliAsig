# Generated by Django 3.0.6 on 2020-05-12 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(default='********', max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Employee',
            new_name='AddEmployee',
        ),
    ]
