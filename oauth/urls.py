
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
app_name = 'oauth'

urlpatterns = [
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^(?P<username>[a-zA-Z0-9]+)/$', views.ProfileView, name='profile'),
]

