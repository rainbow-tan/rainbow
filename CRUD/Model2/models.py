from django.db import models


class DataTable(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    field30 = models.CharField(verbose_name='电务段名称', max_length=200)
    field1 = models.CharField(verbose_name='线别', max_length=200)
    field2 = models.CharField(verbose_name='综合车间', max_length=200)
    field23 = models.CharField(verbose_name='行别', max_length=200)
    field31 = models.CharField(verbose_name='自动闭塞制式', max_length=200)
    field32 = models.CharField(verbose_name='轨道电路制式', max_length=200)
    field33 = models.CharField(verbose_name='自闭区间', max_length=200)
    field3 = models.CharField(verbose_name='车站', max_length=200)
    field34 = models.CharField(verbose_name='车站联锁制式', max_length=200)
    field35 = models.CharField(verbose_name='区间轨道电路名称', max_length=200)
    field36 = models.CharField(verbose_name='是否站联区段', max_length=200)
    field37 = models.CharField(verbose_name='标称载频', max_length=200)
    field38 = models.CharField(verbose_name='区段长度(m)', max_length=200)
    field39 = models.CharField(verbose_name='电容数量', max_length=200)
    field40 = models.CharField(verbose_name='防护信号机名称', max_length=200)
    field41 = models.CharField(verbose_name='是否容许信号', max_length=200)
    field42 = models.CharField(verbose_name='方向电路制式', max_length=200)
    field43 = models.CharField(verbose_name='发送冗余方式', max_length=200)
    field44 = models.CharField(verbose_name='接收冗余方式', max_length=200)
    field45 = models.CharField(verbose_name='大修年', max_length=200)


class Field36Table(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    field1 = models.CharField(verbose_name='是否站联区段', max_length=200)


class Field37Table(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    field1 = models.CharField(verbose_name='标称载频', max_length=200)


class Field41Table(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    field1 = models.CharField(verbose_name='是否容许信号', max_length=200)


class Field42Table(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    field1 = models.CharField(verbose_name='方向电路制式', max_length=200)
