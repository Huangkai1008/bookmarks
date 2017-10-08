from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, logout_then_login, password_change, password_change_done

urlpatterns = [
    # 登入登出
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    # dashboard
    url(r'^$', views.dashboard, name='dashboard'),
    # 修改密码
    url(r'^password-change/$', password_change, name='password_change'),
    url(r'^password-change/done/$', password_change_done, name='password_change_done'),
]