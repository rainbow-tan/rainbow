# Generated by Django 3.0.8 on 2020-12-15 06:59

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0003_auto_20201215_1426'),
        ]
    atomic = False
    operations = [
        migrations.RemoveField(
                model_name='sex',
                name='gender',
                ),
        migrations.AddField(
                model_name='sex',
                name='name',
                field=models.CharField(default='', max_length=100, unique=True, verbose_name='性别'),
                ),
        migrations.AlterField(
                model_name='basicinfo',
                name='exam_area',
                field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                        to='app.ExamArea', to_field='name', verbose_name='考区'),
                ),
        migrations.AlterField(
                model_name='basicinfo',
                name='faculty',
                field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                        to='app.Faculty', to_field='name', verbose_name='学院'),
                ),
        migrations.AlterField(
                model_name='basicinfo',
                name='language',
                field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                        to='app.Language', to_field='name', verbose_name='语种'),
                ),
        migrations.AlterField(
                model_name='basicinfo',
                name='nationality',
                field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                        to='app.Nationality', to_field='name', verbose_name='名族'),
                ),
        migrations.AlterField(
                model_name='basicinfo',
                name='number',
                field=models.CharField(max_length=20, primary_key=True, serialize=False,
                                       verbose_name='学号'),
                ),
        migrations.AlterField(
                model_name='basicinfo',
                name='sex',
                field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Sex',
                                        to_field='name', verbose_name='性别'),
                ),
        migrations.AlterField(
                model_name='examarea',
                name='name',
                field=models.CharField(default='', max_length=100, unique=True,
                                       verbose_name='考区名称'),
                ),
        migrations.AlterField(
                model_name='faculty',
                name='name',
                field=models.CharField(default='', max_length=100, unique=True,
                                       verbose_name='学院名称'),
                ),
        migrations.AlterField(
                model_name='language',
                name='name',
                field=models.CharField(default='', max_length=100, unique=True,
                                       verbose_name='语种名称'),
                ),
        migrations.AlterField(
                model_name='nationality',
                name='name',
                field=models.CharField(default='', max_length=100, unique=True,
                                       verbose_name='名族名称'),
                ),
        migrations.AlterModelTable(
                name='examarea',
                table='Kaoqu',
                ),
        migrations.AlterModelTable(
                name='language',
                table='YuZhong',
                ),
        migrations.AlterModelTable(
                name='nationality',
                table='MingZu',
                ),
        ]
