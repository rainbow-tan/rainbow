# Generated by Django 3.0.8 on 2020-10-13 01:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Model3', '0003_auto_20201011_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field71Table',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                ('field1', models.CharField(max_length=200)),
            ],
        ),
    ]