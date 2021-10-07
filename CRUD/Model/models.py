from django.db import models


# Create your models here.
class DataTable(models.Model):
    auto_id = models.AutoField(primary_key=True)
    field1 = models.CharField(verbose_name='线别', max_length=200)
    field2 = models.CharField(verbose_name='综合车间', max_length=200)
    field3 = models.CharField(verbose_name='车站及区间名称', max_length=200)
    field4 = models.CharField(verbose_name='设备名称', max_length=200)
    field5 = models.CharField(verbose_name='公里标', max_length=200)
    field6 = models.CharField(verbose_name='本线高度', max_length=200)
    field7 = models.CharField(verbose_name='距本线中心线距离(实测值)', max_length=200)
    field8 = models.CharField(verbose_name='距邻线中心线距离(实测值)', max_length=200)
    field9 = models.CharField(verbose_name='临线高度', max_length=200)
    field10 = models.CharField(verbose_name='曲线半径', max_length=200)
    field11 = models.CharField(verbose_name='曲线外轨超高', max_length=200)
    field12 = models.CharField(verbose_name='本线曲线内侧', max_length=200)
    field13 = models.CharField(verbose_name='本线曲线外侧', max_length=200)
    field14 = models.CharField(verbose_name='邻线曲线内侧', max_length=200)
    field15 = models.CharField(verbose_name='邻线曲线外侧', max_length=200)
    field16 = models.CharField(verbose_name='本线标准值', max_length=200)
    field17 = models.CharField(verbose_name='邻线标准值', max_length=200)
    field18 = models.CharField(verbose_name='备注', max_length=200)
    field19 = models.CharField(verbose_name='本线实测值与标准值只差', max_length=200)
    field20 = models.CharField(verbose_name='邻线实测值与标准值只差', max_length=200)
    field21 = models.CharField(verbose_name='本线数据是否超限', max_length=200)
    field22 = models.CharField(verbose_name='邻线数据是否超限', max_length=200)
    field24 = models.CharField(verbose_name='站内或区间', max_length=200)
    field25 = models.CharField(verbose_name='参考标准', max_length=200)
    field26 = models.CharField(verbose_name='有无防撞强', max_length=200)
    field27 = models.CharField(verbose_name='建筑设备类型', max_length=200)
    field28 = models.CharField(verbose_name='核对日期', max_length=200)
    field29 = models.CharField(verbose_name='核对人', max_length=200)
    field70 = models.CharField(verbose_name='线间距', max_length=200)


class Field1Table(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    field1 = models.CharField(verbose_name='线别', max_length=200, unique=True)

    def __str__(self):
        return self.field1


class Field2Table(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    field1 = models.CharField(verbose_name='综合车间', max_length=200, unique=True)

    def __str__(self):
        return self.field1


class Field3Table(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    field1 = models.CharField(verbose_name='车站及区间名称', max_length=200)


class Field23Table(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    field1 = models.CharField(verbose_name='行别', max_length=200)


class Field24Table(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    field1 = models.CharField(verbose_name='站内或区间', max_length=200)


class Field25Table(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    field1 = models.CharField(verbose_name='参考标准', max_length=200)


class Field26Table(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    field1 = models.CharField(verbose_name='有无防撞强', max_length=200)


class Field27Table(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    field1 = models.CharField(verbose_name='建筑设备类型', max_length=200)
