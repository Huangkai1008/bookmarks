from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
    创建一个登录表单
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """
    创建一个注册表单
    """
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='重复密码',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']



