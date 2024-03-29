"""cncryo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gasnews import views as gview
from daily import views as dview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',gview.index),
    path('detail/<int:id>',gview.news_detail),
    path('trans/<int:id>',gview.trans_news_detail),
    path('delete/<int:id>',gview.delete_news,name="delete_news"),
    path('deletebaidu/<int:id>',gview.delete_baidu_news,name="delete_baidu"),
    path('daily/',dview.daily_viwe,name='get_daily')
]
