from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView

from My_project.models import Sign
from UserProfiles_app.models import UserProfile


class SignListView(ListView):
    """通用视图"""
    model = Sign     #指定类
    context_object_name = 'signs'    #courses被传到模板中
    template_name = "My_project/Sign_list.html"  #渲染页面
    def get_queryset(self):
        my_user = get_object_or_404(UserProfile, user=self.request.user)
        signs = Sign.objects.filter(my_user=my_user)
        return signs