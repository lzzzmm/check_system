from allauth.account.forms import ResetPasswordKeyForm
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives


class MySetPasswordForm(ResetPasswordKeyForm):
    def send_email(self, to_email):
        subject = 'Password changed successfully'
        body = 'Your password has been changed successfully'
        email = EmailMultiAlternatives(subject, body, None, [to_email])
        email.send()

    def save(self, commit=True):
        if commit:
            email_field_name = User.get_email_field_name()
            user_email = getattr(self.user, email_field_name)
            self.send_email(user_email)
        super().save_(commit=commit)

