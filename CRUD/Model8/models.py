from django.db import models


class DataTable(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    wentiriqi = models.CharField(verbose_name='检测发现问题日期', max_length=100, default='', null=True)
    xianbie = models.CharField(verbose_name='线别', max_length=100, default='', null=True)
    chejian = models.CharField(verbose_name='综合车间', max_length=100, default='', null=True)
    chezhan = models.CharField(verbose_name='车站', max_length=100, default='', null=True)
    quduan = models.CharField(verbose_name='区段名称', max_length=100, default='', null=True)
    buliangdianrong = models.CharField(verbose_name='发现问题(不良电容)', max_length=100, default='',
                                       null=True)
    hangbie = models.CharField(verbose_name='行别', max_length=100, default='', null=True)
    dianrongshuliang = models.CharField(verbose_name='本区段电容数量', max_length=100, default='',
                                        null=True)
    zaiping = models.CharField(verbose_name='载频', max_length=100, default='', null=True)
    chuliriqi = models.CharField(verbose_name='处理日期', max_length=100, default='', null=True)
    yuanying = models.CharField(verbose_name='问题原因', max_length=100, default='', null=True)
    chuliqingkuang = models.CharField(verbose_name='处理情况', max_length=100, default='', null=True)
    shangbaoqingkuang = models.CharField(verbose_name='上报情况', max_length=100, default='', null=True)
    zhouqi = models.CharField(verbose_name='周期', max_length=100, default='', null=True)
    beizhu = models.CharField(verbose_name='备注', max_length=100, default='', null=True)
    qiandianliu = models.CharField(verbose_name='整改前电流(A)', max_length=100, default='', null=True)
    houdianliu = models.CharField(verbose_name='整改后电流(A)', max_length=100, default='', null=True)
    qiandianya = models.CharField(verbose_name='整改前电压(V)', max_length=100, default='', null=True)
    houdianya = models.CharField(verbose_name='整改后电压(V)', max_length=100, default='', null=True)
    qiandianrong = models.CharField(verbose_name='整改前容值(uf)', max_length=100, default='', null=True)
    houdianrong = models.CharField(verbose_name='整改后容值(uf)', max_length=100, default='', null=True)
    changjia = models.CharField(verbose_name='生产厂家', max_length=100, default='', null=True)
    shiyongshijian = models.CharField(verbose_name='使用时间(年)', max_length=100, default='', null=True)
    fankuiren = models.CharField(verbose_name='反馈人', max_length=100, default='', null=True)


class QuDuanTable(models.Model):
    auto_id = models.AutoField(verbose_name='序号', primary_key=True)
    xianbie = models.CharField(verbose_name='线别', max_length=100, default='', null=True, blank=True)
    chezhan = models.CharField(verbose_name='车站', max_length=100, default='', null=True, blank=True)
    quduan = models.CharField(verbose_name='区段名称', max_length=100, default='', null=True,
                              blank=True)
    zaiping = models.CharField(verbose_name='载频', max_length=100, default='', null=True, blank=True)
    dianrongshuliang = models.CharField(verbose_name='电容数量', max_length=100, default='', null=True,
                                        blank=True)
    hangbie = models.CharField(verbose_name='行别', max_length=100, default='', null=True, blank=True)
    quduanchangdu = models.CharField(verbose_name='区段长度', max_length=100, default='', null=True,
                                     blank=True)
