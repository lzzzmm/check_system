from django.db import models

# Create your models here.

class Department(models.Model):
    ID_department = models.CharField(max_length=50, verbose_name='部门编号', null=True, unique=True)
    department = models.CharField(max_length=50, verbose_name='部门名称', null=True)
    Details = models.TextField(max_length=1000, verbose_name='部门简介', null=True)

    class Meta:
        verbose_name = '部门信息',
        verbose_name_plural = '部门信息'

    def __str__(self):
        return self.department



class Position(models.Model):
    ID_position = models.CharField(max_length=50, verbose_name='工作岗位编号', null=True, unique=True)
    ID_department = models.ForeignKey(Department, verbose_name='归属部门', on_delete=models.CASCADE)
    position = models.CharField(max_length=50, verbose_name='工作岗位', null=True)
    Details = models.TextField(max_length=1000, verbose_name='工作岗位职责', null=True)

    class Meta:
        verbose_name = '工作岗位信息',
        verbose_name_plural = '工作岗位信息'

    def __str__(self):
        return self.position
