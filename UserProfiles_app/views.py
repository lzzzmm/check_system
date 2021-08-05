from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView

from UserProfiles_app.models import UserProfile


class mymessage(DetailView):
    model = UserProfile
    template_name = 'UserProfile/mymessage.html'

    def post(self, request, pk):
        user = request.user
        user_post = request.POST
        user_profile = get_object_or_404(UserProfile, user=user)
        user_profile.name = user_post['name']
        user_profile.gender = user_post['gender']
        user_profile.ID_number = user_post['ID_number']
        user_profile.political_landscape = user_post['political_landscape']
        user_profile.address = user_post['address']
        user_profile.phone = user_post['phone']
        user_profile.education = user_post['education']
        user_profile.bank_card = user_post['bank_card']
        user_profile.save()
        return redirect('mymessage', pk=user.id)

@login_required
def updatemessage(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'UserProfile/updatemessage.html', {'user_profile': user_profile})