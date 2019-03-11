# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from gasnews.get_news.gasnews.model import *
from bs4 import BeautifulSoup as bs

# Create your views here.


def index(request):
    newslist = News.select().where(News.lang == 'zh').order_by(News.add_date.desc())[:30]
    baidu_news_list = SearchNews.select().order_by(SearchNews.add_date.desc())[:80]
    english_news = News.select().where(News.lang.contains('en')).order_by(News.add_date.desc())[:30]
    trans_news = TransNews.select().order_by(TransNews.add_date.desc())[:30]

    context = {'newslist': newslist, 'baidu': baidu_news_list, 'english_news': english_news, 'trans_news': trans_news}

    return render(request, 'index.html', context)


def news_detail(request, id):
    #article = ""
    news_text = News.select().where(News.id == id)
    title = news_text[0].title
    link = news_text[0].source
    # news_text = bs(news_text[0].text, 'lxml')
    # p_list = news_text.find_all('p')
    # for p in p_list:
    #     article = article + p.text + "<br>"
    article=news_text[0].text

    return render(request, 'news_detail.html', {'article': article, 'title': title, 'link': link})


def trans_news_detail(request, id):
    news_text = TransNews.select().where(TransNews.id == id)
    title = news_text[0].title
    article = news_text[0].text
    link = news_text[0].source

    return render(request, 'news_detail.html', {'article': article, 'title': title, 'link': link})


def delete_news(request,id):
    News.delete().where(News.id==id).execute()
    return HttpResponseRedirect('/')

def delete_baidu_news(request,id):
    SearchNews.delete().where(SearchNews.id==id).execute()
    return HttpResponseRedirect('/')
