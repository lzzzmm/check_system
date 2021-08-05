from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from Other_Dao.models import Department, Position

Sex=[
    ('男', '男'),
    ('女', '女')
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='关联用户', on_delete=models.CASCADE)
    name = models.CharField(max_length=135, verbose_name=u'姓名', blank=True, null=True)
    gender = models.CharField(max_length=135, choices=Sex, verbose_name=u'性别', blank=True, null=True)
    ID_number = models.CharField(max_length=18, verbose_name="身份证号码", null=True)
    political_landscape = models.CharField(max_length=50, verbose_name='政治面貌', blank=True, null=True)
    address = models.CharField(max_length=135, verbose_name='住址', blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name='手机号码', null=True)
    ID_department = models.ForeignKey(Department, verbose_name='归属部门', null=True, on_delete=models.SET_NULL, blank=True)
    ID_position = models.ForeignKey(Position, verbose_name='岗位', null=True, on_delete=models.SET_NULL, blank=True)
    education = models.CharField(max_length=50, verbose_name='学历', blank=True, null=True)
    enter_time = models.DateField(auto_now_add=True, verbose_name="入职时间")
    base_salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='基本薪资', null=True)
    bank_card = models.CharField(max_length=50, verbose_name='银行卡号', null=True)
    notes = models.TextField(max_length=500, verbose_name="备注", blank=True, null=True)
    modified_date = models.DateField(auto_now=True, verbose_name='最后修改时间')

    class Meta:
        verbose_name = '扩展信息',
        verbose_name_plural = '扩展信息'

    def __str__(self):
        return self.name




