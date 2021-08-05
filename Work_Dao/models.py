from django.db import models

# Create your models here.
from django.utils.html import format_html

from UserProfiles_app.models import UserProfile

HANDLE_TYPES = (
    ('未处理', '未处理'),
    ("已同意", '已同意'),
    ('已拒绝', '已拒绝'),
)

Note_type = (
    ('已完成', '已完成'),
    ('未处理', '未处理'),
)

Task_handle_type = (
    ('已完成', '已完成'),
    ('未处理', '未处理'),
    ('转接', '转接'),
)

class Apply(models.Model):
    applicant = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE, related_name='applicant_UserProfile', verbose_name='申请人')
    detail = models.TextField(max_length=1000, verbose_name='申报信息', null=True)
    apply_day = models.DateField(auto_now_add=True, verbose_name="申报时间")
    process_status = models.CharField( max_length=20, choices=HANDLE_TYPES, null=True, default='未处理', verbose_name='处理状态')
    hander = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL, related_name='Apply_hander_UserProfile', verbose_name='处理人')
    process_day = models.DateField(auto_now=True, verbose_name="处理时间")
    reply = models.TextField(max_length=1000, verbose_name='回复', null=True)

    class Meta:
        verbose_name = '申报表',
        verbose_name_plural = '申报表'

    def HANDLE_TYPES_CLODR(self):
        if self.process_status == "未处理":
            color_code = 'black'
        elif self.process_status == "已同意":
            color_code = 'green'
        else:
            color_code = 'red'
        return format_html('<span style="color:{};">{}</span>', color_code, self.process_status)

    HANDLE_TYPES_CLODR.short_description = '处理状态'


    def __str__(self):
        return self.applicant.name



class Advise(models.Model):
    proposer = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE, related_name='proposer_UserProfile',verbose_name='提出者')
    advise = models.TextField(max_length=1000, verbose_name='建议', null=True)
    submit_time = models.DateField(auto_now_add=True, verbose_name="提交时间")
    status = models.CharField( max_length=20, choices=HANDLE_TYPES,  default='未处理', verbose_name='处理状态')
    feedback = models.TextField(max_length=1000, verbose_name='反馈', null=True)
    hander = models.ForeignKey(UserProfile, verbose_name='处理人', null=True, on_delete=models.SET_NULL, related_name='Advise_hander_UserProfile')
    process_day = models.DateField(auto_now=True, verbose_name="处理时间")

    class Meta:
        verbose_name = '投递建议',
        verbose_name_plural = '投递建议'

    def HANDLE_TYPES_CLODR(self):
        if self.status == "未处理":
            color_code = 'black'
        elif self.status == "已同意":
            color_code = 'green'
        else:
            color_code = 'red'
        return format_html('<span style="color:{};">{}</span>', color_code, self.status)

    HANDLE_TYPES_CLODR.short_description = '处理状态'

    def __str__(self):
        return self.proposer.name


class Task_list(models.Model):
    Distributor = models.ForeignKey(UserProfile, verbose_name='分配人', null=True, on_delete=models.SET_NULL, related_name='Distributor_UserProfile')
    detail = models.TextField(max_length=500, verbose_name='任务内容', null=True)
    closing_day = models.DateTimeField(verbose_name='截止时间')
    modify_day = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    notice_day = models.DateTimeField(auto_now_add=True, verbose_name="通知时间")
    people_work = models.ForeignKey(UserProfile, verbose_name='指定员工', null=True, on_delete=models.SET_NULL, related_name='people_work_UserProfile')
    status = models.CharField( max_length=20, choices=Task_handle_type, default='未处理', verbose_name='完成状态')

    class Meta:
        verbose_name = '任务清单',
        verbose_name_plural = '任务清单'

    def Task_handle_type_CLODR(self):
        if self.status == "未处理":
            color_code = 'black'
        elif self.status == "已完成":
            color_code = 'green'
        else:
            color_code = 'blue'
        return format_html('<span style="color:{};">{}</span>', color_code, self.status)

    Task_handle_type_CLODR.short_description = '处理状态'

    def __str__(self):
        return self.detail[:10]


class Note(models.Model):
    creator = models.ForeignKey(UserProfile, verbose_name='创建人', null=True, on_delete=models.CASCADE,
                                    related_name='creator_UserProfile')
    reminder_time = models.DateTimeField(verbose_name="提醒时间", blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modify_time = models.DateTimeField( auto_now=True, verbose_name="修改时间", blank=True, null=True)
    note = models.TextField(max_length=1000, verbose_name='便签内容', null=True)
    status = models.CharField(max_length=20, choices=Note_type, default='未处理', verbose_name='完成状态')

    class Meta:
        verbose_name = '便签',
        verbose_name_plural = '便签'
        ordering = ['-create_time']

    def Note_type_CLODR(self):
        if self.status == "未处理":
            color_code = 'black'
        else :
            color_code = 'green'
        return format_html('<span style="color:{};">{}</span>', color_code, self.status)

    Note_type_CLODR.short_description = '处理状态'

    def __str__(self):
        list_note = self.note.split()
        name_note = ''.join(list_note)
        return name_note[:10]







