from django import forms


class LoginForm(forms.Form):
    """
    创建一个登录表单
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
