from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.conf import settings
from django.db import models
from django.template.loader import render_to_string

# Create your models here.

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    #phone_number = models.PhoneNumberField(_(""))
    phone_number = models.CharField(max_length = 15, blank=True,
                                    validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")])
    gender = models.CharField(max_length=1, blank=True,
                              choices=GenderChoices.choices)
    profile_image = models.ImageField(blank=True, upload_to="accounts/profile_image/%Y/%m/%d/%H/%M/%S",
                                      help_text="360px * 360px 이하의 png/jpg 파일을 업로드 해주세요.")
    # django-imagekit 라이브러리 사용해서 서버단에서 편하게 처리 가능.


    def send_welcome_email(self):
        subject = render_to_string("accounts/welcome_email_subject.txt", {
            "user": self,}) # "Djangostagram 가입을 환영합니다."
        content = render_to_string("accounts/welcome_email_content.txt", {
            "user": self,}) # """lalalalalala"""
        
        sender_email = settings.WELCOME_EMAIL_SENDER
        send_mail(subject, content, sender_email, [self.email], fail_silently=False)