from django.db import models

# Create your models here.
from UserProfiles_app.models import UserProfile

SIGN_TYPES = (
    ('签到成功', '签到成功'),
    ("暂未签到", '暂未签到'),
)

class Sign(models.Model):
    my_user = models.ForeignKey(UserProfile, verbose_name='签到人', on_delete=models.CASCADE)
    sign_status = models.CharField( max_length=20, choices=SIGN_TYPES, default='暂未签到', verbose_name='签到状态')
    sign_time = models.DateTimeField(auto_now_add=True, verbose_name="签到时间")


    class Meta:
        verbose_name = '签到',
        verbose_name_plural = '签到'

    def __str__(self):
        return self.my_user.name


