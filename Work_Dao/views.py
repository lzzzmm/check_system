

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View
from django.views.generic import DetailView

from UserProfiles_app.models import UserProfile
from Work_Dao.models import Note, Task_list, Apply


class profile(LoginRequiredMixin, View):

    def get(self, request):
        creator = get_object_or_404(UserProfile, user=request.user)
        notes = Note.objects.filter(creator=creator)
        return render(request, 'account/profile.html',{'notes': notes})

    def post(self, request):  # 增加
        user = request.user
        creator = get_object_or_404(UserProfile, user=user)
        request_Note = request.POST
        note = request_Note['note']
        reminder_time = request_Note['reminder_time']
        if reminder_time == "":
            create_note = Note(creator=creator, note=note)
        else:
            create_note = Note(creator=creator, reminder_time=reminder_time, note=note)
        create_note.save()
        return redirect('profile')

@login_required
def update_note(request, id):
    note = Note.objects.get(id=id)
    note.note = request.POST['note']
    if request.POST['reminder_time'] != "":
        note.reminder_time = request.POST['reminder_time']
    else:
        note.reminder_time = None
    note.status = request.POST['status']
    note.save()
    return redirect('profile')

@login_required
def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('profile')

# -----------------------------------------------------------------------------------------------

class Task_list_wait(LoginRequiredMixin, View):
    def get(self,request):
        Distributor_or_people_work = get_object_or_404(UserProfile, user=request.user)
        task_lists = Task_list.objects.filter(Q(Distributor=Distributor_or_people_work) | Q(people_work=Distributor_or_people_work) & Q(status="未处理"))
        return render(request, 'Work_Dao/Task_list_wait.html', {'task_lists': task_lists})

    def post(self, request):
        return redirect('Task_list_wait')


class Task_detail(DetailView):
    model = Task_list
    template_name = 'Work_Dao/task_detail.html'


@login_required
def update_task_detail(request):
    user = request.user
    Distributor = get_object_or_404(UserProfile, user=user)
    status = request.POST['status']
    task = Task_list.objects.get(id=request.POST['task'])

    if status == "转接":
        people_work_get = User.objects.get(username=request.POST['people_work'])
        people_work = get_object_or_404(UserProfile, user=people_work_get)
        task_detail = Task_list(Distributor=Distributor, detail=task.detail, closing_day=task.closing_day, people_work=people_work )
        task_detail.save()
    else:
        pass
    task.status = status
    task.save()
    return redirect('Task_list_wait')


class Task_history(LoginRequiredMixin, View):

    def get(self, request):
        Distributor_or_people_work = get_object_or_404(UserProfile, user=request.user)
        task_lists = Task_list.objects.filter(Q(Distributor=Distributor_or_people_work) | Q(people_work=Distributor_or_people_work) & Q(status__in=["已完成", '转接']))
        return render(request, 'Work_Dao/task_history.html',{'task_lists': task_lists})


@login_required
def delete_task_history(request, id):
    task = Task_list.objects.get(id=id)
    task.delete()
    return redirect('Task_history')


# ----------------------------------------------申报-------------------------------------------------
@login_required
def Add_apply(request):
    if request.method == 'GET':
        return render(request, 'Work_Dao/Apply.html')

    if request.method == 'POST':
        user = request.user
        applicant = get_object_or_404(UserProfile, user=user)
        detail = request.POST['detail']
        apply = Apply(applicant=applicant, detail=detail)
        apply.save()
        return redirect('Add_apply')

@login_required
def Apply_history(request):
    if request.method == 'GET':
        applicant_or_hander = get_object_or_404(UserProfile, user=request.user)
        applys = Apply.objects.filter(Q(applicant=applicant_or_hander) | Q(hander=applicant_or_hander))
        return render(request, 'Work_Dao/apply_list.html', {'applys': applys})

@login_required
def delete_apply(request, id):
    apply = get_object_or_404(Apply, id=id)
    apply.delete()
    return redirect("Apply_history")

class apply_detail(DetailView):
    model = Apply
    template_name = 'Work_Dao/apply_detail.html'



def update_apply(request, id):
    apply = get_object_or_404(Apply, id=id)
    if request.method == "GET":
        return render(request, "Work_Dao/update_apply.html", {'apply':apply})
    else:
        apply_detail = request.POST['detail']
        apply.detail = apply_detail
        apply.save()
        return redirect('Apply_history')





