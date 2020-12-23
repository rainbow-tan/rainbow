from django.db import models


# 学院
class Faculty(models.Model):
    number = models.AutoField('学院编号', primary_key=True)
    name = models.CharField(
            verbose_name='学院名称',  # 显示的名称
            unique=True,  # 唯一性,默认False
            blank=False,  # 表单是否可为空,默认False
            null=False,  # 数据库是否保存null,默认False
            default='',  # 默认保存数据
            max_length=100
            )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "XueYuan"


# 考区
class ExamArea(models.Model):
    number = models.AutoField('考区编号', primary_key=True)
    name = models.CharField(
            verbose_name='考区名称',  # 显示的名称
            unique=True,  # 唯一性,默认False
            blank=False,  # 表单是否可为空,默认False
            null=False,  # 数据库是否保存null,默认False
            default='',  # 默认保存数据
            max_length=100
            )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Kaoqu"


# 外语语种
class Language(models.Model):
    number = models.AutoField('语种编号', primary_key=True)
    name = models.CharField(
            verbose_name='语种名称',  # 显示的名称
            unique=True,  # 唯一性,默认False
            blank=False,  # 表单是否可为空,默认False
            null=False,  # 数据库是否保存null,默认False
            default='',  # 默认保存数据
            max_length=100
            )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "YuZhong"


# 名族
class Nationality(models.Model):
    number = models.AutoField('名族编号', primary_key=True)
    name = models.CharField(
            verbose_name='名族名称',  # 显示的名称
            unique=True,  # 唯一性,默认False
            blank=False,  # 表单是否可为空,默认False
            null=False,  # 数据库是否保存null,默认False
            default='',  # 默认保存数据
            max_length=100
            )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "MingZu"


# 性别
class Sex(models.Model):
    number = models.AutoField('编号', primary_key=True)
    name = models.CharField(
            verbose_name='性别',  # 显示的名称
            unique=True,  # 唯一性,默认False
            blank=False,  # 表单是否可为空,默认False
            null=False,  # 数据库是否保存null,默认False
            default='',  # 默认保存数据
            max_length=100
            )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Sex"


# 基础信息
class BasicInfo(models.Model):
    number = models.CharField(verbose_name='学号', max_length=20, primary_key=True, )
    name = models.CharField(verbose_name='姓名', max_length=50, )
    sex = models.ForeignKey(verbose_name='性别', to="Sex", to_field='name', on_delete=models.CASCADE)
    faculty = models.ForeignKey(verbose_name='学院', to="Faculty", to_field='name',
                                on_delete=models.CASCADE)
    class_name = models.CharField(verbose_name='班级', max_length=50, )
    exam_area = models.ForeignKey(verbose_name='考区', to="ExamArea", to_field='name',
                                  on_delete=models.CASCADE)
    into_date = models.DateField(verbose_name='入学时间', )
    language = models.ForeignKey(verbose_name='语种', to="Language", to_field='name', blank=False,
                                 on_delete=models.CASCADE)
    birthday = models.DateField(verbose_name='出生日期', )
    nationality = models.ForeignKey(verbose_name='名族', to="Nationality", to_field='name',
                                    on_delete=models.CASCADE)
    grade = models.FloatField(verbose_name='分数', )
    email = models.EmailField(verbose_name='邮箱', blank=True)

    def __str__(self):
        return self.number

    class Meta:
        db_table = "BasicInfo"
