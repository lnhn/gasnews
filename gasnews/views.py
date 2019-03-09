# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from gasnews.get_news.gasnews.model import *
from bs4 import BeautifulSoup as bs


# Create your views here.


def index(request):
    newslist = News.select().where(News.lang == 'zh').order_by(News.pub.desc())[:30]
    baidu_news_list = SearchNews.select().order_by(SearchNews.add_date.desc())[:50]
    english_news = News.select().where(News.lang.contains('en')).order_by(News.pub.desc())[:30]
    trans_news = TransNews.select().order_by(TransNews.pub.desc())[:30]

    context = {'newslist': newslist, 'baidu': baidu_news_list, 'english_news': english_news, 'trans_news': trans_news}

    return render(request, 'index.html', context)


def news_detail(request,id):
    article=""
    news_text=News.select().where(News.id==id)
    title=news_text[0].title
    link=news_text[0].source
    news_text=bs(news_text[0].text,'lxml')
    p_list=news_text.find_all('p')
    for p in p_list:
        article=article+p.text+"\n"
    
    return render(request,'news_detail.html',{'article':article,'title':title,'link':link})


def trans_news_detail(request,id):
     
    news_text=TransNews.select().where(TransNews.id==id)
    title=news_text[0].title
    article=news_text[0].text
    link=news_text[0].source
    
    return render(request,'news_detail.html',{'article':article,'title':title,'link':link})