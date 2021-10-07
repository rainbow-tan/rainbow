from django.db import models

"""
python manage.py makemigrations
python manage.py migrate
"""


class Luruye(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    duanbie = models.CharField(verbose_name='段别', max_length=100, default='', null=True)
    xianbie = models.CharField(verbose_name='线别', max_length=100, default='', null=True)
    chejian = models.CharField(verbose_name='车间', max_length=100, default='', null=True)
    chezhan = models.CharField(verbose_name='车站', max_length=100, default='', null=True)
    genbanren = models.CharField(verbose_name='车间跟班人', max_length=100, default='', null=True)
    gongqu = models.CharField(verbose_name='工区', max_length=100, default='', null=True)
    zuoyeren = models.CharField(verbose_name='工区作业人', max_length=100, default='', null=True)
    renwuliang = models.CharField(verbose_name='任务量', max_length=100, default='', null=True)
    xiangmu = models.CharField(verbose_name='项目', max_length=100, default='', null=True)
    fenlei = models.CharField(verbose_name='工作内容分类', max_length=100, default='', null=True)
    yuefen = models.CharField(verbose_name='工作月份', max_length=100, default='', null=True)
    gongzuoneirong = models.CharField(verbose_name='工作内容', max_length=100, default='', null=True)
    zhouqi = models.CharField(verbose_name='工作周期', max_length=100, default='', null=True)
    neirongshuoming = models.CharField(verbose_name='工作要求说明', max_length=100, default='', null=True)
    danwei = models.CharField(verbose_name='单位', max_length=100, default='', null=True)
    wanchengshuliang = models.CharField(verbose_name='完成数量', max_length=100, default='', null=True)
    wanchengriqi = models.CharField(verbose_name='完成日期', max_length=100, default='', null=True)


class ZhuYe(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    xiangmu = models.CharField(verbose_name='项目', max_length=100, default='', null=True)
    fenlei = models.CharField(verbose_name='工作内容分类', max_length=100, default='', null=True)
    yuefen = models.CharField(verbose_name='工作月份', max_length=100, default='', null=True)
    zhouqi = models.CharField(verbose_name='工作周期', max_length=100, default='', null=True)
    neirongshuoming = models.CharField(verbose_name='工作要求说明', max_length=100, default='', null=True)
    danwei = models.CharField(verbose_name='单位', max_length=100, default='', null=True)
    renwuliang = models.CharField(verbose_name='任务量', max_length=100, default='', null=True)
    benyuewanchen = models.CharField(verbose_name='本月完成数量', max_length=100, default='', null=True)
    leijiwanchen = models.CharField(verbose_name='累计完成数量', max_length=100, default='', null=True)
    xianbie = models.CharField(verbose_name='线别', max_length=100, default='', null=True)
    chejian = models.CharField(verbose_name='车间', max_length=100, default='', null=True)
    chezhan = models.CharField(verbose_name='车站', max_length=100, default='', null=True)
    create_time = models.CharField(verbose_name='创建时间', max_length=100, default='', null=True)


class XiangMu(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    xiangmu = models.CharField(verbose_name='项目', max_length=100, default='', null=True)
    fenlei = models.CharField(verbose_name='工作内容分类', max_length=100, default='', null=True)
    yuefen = models.CharField(verbose_name='工作月份', max_length=100, default='', null=True)
    zhouqi = models.CharField(verbose_name='工作周期', max_length=100, default='', null=True)
    neirongshuoming = models.CharField(verbose_name='工作要求说明', max_length=100, default='', null=True)
    danwei = models.CharField(verbose_name='单位', max_length=100, default='', null=True)
