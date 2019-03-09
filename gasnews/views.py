# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from gasnews.get_news.gasnews.model import *



# Create your views here.


def index(request):    
    newslist=News.select().where(News.lang=='zh').order_by(News.pub.desc())[:30]
    baidu_news_list=SearchNews.select().order_by(SearchNews.add_date.desc())[:50]
    english_news=News.select().where(News.lang.contains('en')).order_by(News.pub.desc())[:30]
    trans_news=TransNews.select().order_by(TransNews.pub.desc())[:30]

    context={'newslist':newslist,'baidu':baidu_news_list,'english_news':english_news,'trans_news':trans_news}
   
    return render(request,'index.html',context)

def add2(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))
