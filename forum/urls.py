"""verifone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name = "forum"

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^question/(?P<pk>\d+)$', views.QuestionView, name='question'),
    url(r'^search/$', views.search, name='search'),
    url(r'^post/$', views.QuestionCreate.as_view(), name='question-create'),
    url(r'^update/(?P<pk>\d+)$', views.UpdateQuestion.as_view(), name='question-update'),
    url(r'^delete/(?P<pk>\d+)$', views.DeleteQuestion.as_view(), name='question-delete'),
    url(r'^bot/$', views.BotChat, name='bot-chat'),
]
