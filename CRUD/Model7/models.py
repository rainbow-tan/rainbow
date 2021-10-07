from django.db import models


class DataTable(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    xianbie = models.CharField(verbose_name='线别', max_length=100, default='', null=True)
    chejian = models.CharField(verbose_name='综合车间', max_length=100, default='', null=True)
    didian = models.CharField(verbose_name='使用地点', max_length=100, default='', null=True)
    zongcheng = models.CharField(verbose_name='计量器具总称', max_length=100, default='', null=True)
    mingcheng = models.CharField(verbose_name='计量器具名称', max_length=100, default='', null=True)
    bianhao = models.CharField(verbose_name='出产编号', max_length=100, default='', null=True)
    guige = models.CharField(verbose_name='规格型号', max_length=100, default='', null=True)
    dengji = models.CharField(verbose_name='准确度等级', max_length=100, default='', null=True)
    fanwei = models.CharField(verbose_name='测量范围(mm)', max_length=100, default='', null=True)
    changjia = models.CharField(verbose_name='制造厂家', max_length=100, default='', null=True)
    zhuanye = models.CharField(verbose_name='专业', max_length=100, default='', null=True)
    fuzeren = models.CharField(verbose_name='保管负责人', max_length=100, default='', null=True)
    riqi = models.CharField(verbose_name='检定日期', max_length=100, default='', null=True)
    xiaciriqi = models.CharField(verbose_name='下次检定日期', max_length=100, default='', null=True)
    zhouqi = models.CharField(verbose_name='检定周期', max_length=100, default='', null=True)
    dangqianzhuangtai = models.CharField(verbose_name='当前状态', max_length=100, default='', null=True)
    yibiaozhuangtai = models.CharField(verbose_name='仪表状态', max_length=100, default='', null=True)
    beizhu = models.CharField(verbose_name='备注', max_length=100, default='', null=True)


class XianbieChejianChenzhan(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    xianbie = models.CharField(verbose_name='线别', max_length=100, default='', null=True)
    chejian = models.CharField(verbose_name='综合车间', max_length=100, default='', null=True)
    chezhan = models.CharField(verbose_name='车站名称', max_length=100, default='', null=True,
                               unique=True)


class JiliangQiju(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    zongcheng = models.CharField(verbose_name='计量器具总称', max_length=100, default='', null=True,
                                 unique=True)


class JiandingZhouqi(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    zhouqi = models.CharField(verbose_name='检定周期', max_length=100, default='', null=True,
                              unique=True)


class DiDian(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    didian = models.CharField(verbose_name='使用地点', max_length=100, default='', null=True)


class DangqianZhuangtai(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    dangqianzhuangtai = models.CharField(verbose_name='当前状态', max_length=100, default='', null=True)


class ChangJia(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    changjia = models.CharField(verbose_name='生产厂家', max_length=100, default='', null=True)
