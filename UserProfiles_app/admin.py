from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from UserProfiles_app.models import UserProfile

# 定义一个行内 admin
class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = '扩展信息'

# 将 Profile 关联到 User 中
class New_UserAdmin(UserAdmin):
    inlines = (ProfileInline,)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'phone', 'enter_time')
    list_per_page = 30



# 重新注册 User
admin.site.unregister(User)
admin.site.register(User, New_UserAdmin)

admin.site.register(UserProfile, UserProfileAdmin)


#定义后台标题
admin.site.site_header='一滴办公管理后台'
admin.site.site_title='一滴办公管理后台'

