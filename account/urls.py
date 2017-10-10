from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, logout_then_login, password_change, password_change_done
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, \
     password_reset_complete

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
    # 重置密码
    url(r'^password-reset/$', password_reset, name='password_reset'),
    url(r'^password-reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^password-reset/complete/$', password_reset_complete,
        name='password_reset_complete'),
    # 注册
    url(r'^register/$', views.register, name='register'),
    # profile
    url(r'^edit/$', views.edit, name='edit'),
]