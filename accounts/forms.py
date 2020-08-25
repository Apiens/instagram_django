from django import forms
from django.contrib.auth.forms import (UserCreationForm,
                                       PasswordChangeForm as AuthPasswordChangeForm)
from .models import User

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print(self.fields['email'].required)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        print(self.fields['email'].required)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
        return email

# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image', 'first_name', 'last_name', 'website_url', 'bio', 'phone_number', 'gender']

class PasswordChangeForm(AuthPasswordChangeForm):
    def clean_new_password1(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        if old_password == new_password1:
            raise forms.ValidationError("새로운 암호는 기존 암호와 다르게 입력해 주세요.")
        return new_password1

    # def clean_new_password2(self):
    #     old_password = self.cleaned_data.get('old_password')
    #     new_password2 = super().clean_new_password2()
    #     if old_password == new_password2:
    #         raise forms.ValidationError("새로운 암호는 기존 암호와 다르게 입력해 주세요.")
    #     return new_password2 
    