# Generated by Django 3.0.6 on 2020-05-12 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_auto_20200511_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comp_regCode', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('Comp_name', models.CharField(default='insert a name', max_length=20)),
                ('Comp_domain', models.CharField(default='EX: IT domain', max_length=40)),
                ('Cust_address', models.TextField(default='some address')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalCustomer',
            fields=[
                ('Cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('Cust_name', models.CharField(default='insert a name', max_length=20)),
                ('Cust_email', models.CharField(default='sth@upb.ro', max_length=40)),
                ('Cust_feed', models.TextField(default='some feedback')),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
