from django.db import models


class PartTable(models.Model):
    sn = models.AutoField(verbose_name='序号', primary_key=True)
    pn = models.CharField(verbose_name='零件号', max_length=100, blank=True, null=True, default='')
    part_name = models.CharField(verbose_name='零件名称', max_length=100, blank=True, null=True,
                                 default='')
    car_type = models.CharField(verbose_name='车型', max_length=100, blank=True, null=True,
                                default='')
    producer = models.CharField(verbose_name='供应商', max_length=100, blank=True, null=True,
                                default='')
    receive_date = models.CharField(verbose_name='到件时间', max_length=100, blank=True, null=True,
                                    default='')
    batch = models.CharField(verbose_name='批次', max_length=100, blank=True, null=True, default='', )
    send_people = models.CharField(verbose_name='送件人', max_length=100, blank=True, null=True,
                                   default='', )
    contact = models.CharField(verbose_name='联系方式', max_length=100, blank=True, null=True,
                               default='', )
    save_count = models.CharField(verbose_name='库存数量', max_length=100, blank=True, null=True,
                                  default='', )
    receive_people = models.CharField(verbose_name='接收人', max_length=100, blank=True, null=True,
                                      default='', )
    deal_mode = models.CharField(verbose_name='处理方式', max_length=100, blank=True, null=True,
                                 default='', )
    deal_count = models.CharField(verbose_name='报废数量', max_length=100, blank=True, null=True,
                                  default='', )
    deal_remark = models.CharField(verbose_name='取走人及电话', max_length=100, blank=True, null=True,
                                   default='', )
    deal_date = models.CharField(verbose_name='取走时间', max_length=100, blank=True, null=True,
                                 default='')
    qrcode = models.CharField(verbose_name='二维码', max_length=100, blank=True, null=True,
                              default='')
    use = models.CharField(verbose_name='零件用途', max_length=100, blank=True, null=True,
                           default='')
