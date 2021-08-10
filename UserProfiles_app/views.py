from allauth.account import app_settings
from allauth.account.adapter import get_adapter
from allauth.account.forms import default_token_generator
from allauth.account.utils import user_pk_to_url_str, perform_login
from allauth.account.views import PasswordResetFromKeyView

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
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

class CustomPasswordResetView(PasswordResetView):
    def post(self, request, *args, **kwargs):
        ID_number = request.POST['ID_number']
        try:
            user = User.objects.get(username=request.POST['username'])
            true_profile = get_object_or_404(UserProfile, user=user)
            user_profile = UserProfile.objects.get(ID_number=ID_number)
            if true_profile == user_profile:
                token_generator = kwargs.get("token_generator", default_token_generator)
                temp_key = token_generator.make_token(user)
                path = reverse("account_reset_password_from_key", kwargs=dict(uidb36=user_pk_to_url_str(user), key=temp_key))
                return redirect(path)
        except:
            messages.add_message(request, messages.ERROR, '信息填写错误！')
            return redirect('CustomPasswordResetView')
    def get(self, request, *args, **kwargs):
        return render(request, 'account/password_reset.html')



class PasswordResetFromKeyViewNew(PasswordResetFromKeyView):
    def form_valid(self, form):
        form.save()
        adapter = get_adapter(self.request)
        if self.reset_user and app_settings.LOGIN_ATTEMPTS_LIMIT:
            # User successfully reset the password, clear any
            # possible cache entries for all email addresses.
            for email in self.reset_user.emailaddress_set.all():
                from_email = None
                subject = '一滴账号重置密码通知'
                text_content = '您好！您在一滴平台上重置了密码，若该操作若非本人操作，请立即联系技术部部门进行处理！.文本'
                html_content = '<p>您好！您在一滴平台上重置了密码，若该操作若非本人操作，请立即联系技术部部门进行处理！.HTML</p>'
                msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                adapter._delete_login_attempts_cached_email(
                    self.request, email=email.email
                )

        adapter.add_message(
            self.request,
            messages.SUCCESS,
            "account/messages/password_changed.txt",
        )
        if app_settings.LOGIN_ON_PASSWORD_RESET:
            print(88)
            return perform_login(
                self.request,
                self.reset_user,
                email_verification=app_settings.EMAIL_VERIFICATION,
            )

        return super(PasswordResetFromKeyView, self).form_valid(form)

password_reset_from_key = PasswordResetFromKeyViewNew.as_view()