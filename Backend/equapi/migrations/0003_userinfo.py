# Generated by Django 2.2.1 on 2019-06-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equapi', '0002_auto_20190531_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('authority_identity', models.CharField(max_length=20)),
                ('celphone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('identity', models.CharField(max_length=20)),
                ('landline', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('phone_cornet', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=10)),
                ('student_number', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]
