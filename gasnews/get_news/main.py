#!/usr/bin/python
import datetime
from gasnews.collect_news import *
from gasnews import collect_news
from gasnews.model import *
from gasnews.collect_data_search import *
#from gasnews.translator import  translate

file=open("log.log",'a')

def get_and_save_news():
    print("start downloading news from websites...",datetime.datetime.now())
    file.writelines("start downloading news from websites..."+str(datetime.datetime.now())+"\n")
    for item in dir(collect_news):
        try:
            if item[:7] == "collect":
                print(item)
                file.writelines(item+"\n")
                news_result = eval(item)()
                today = datetime.datetime.today().date()
                yesterday=today+datetime.timedelta(days=-1)
                data_saved=News.select().where((News.pub==today)|(News.pub==yesterday))
                title=[]

                if  data_saved.__len__() != 0:
                    for t in data_saved:
                        title.append(t.title)

                if news_result != None:
                    for article in news_result:
                        if not article['article_title'] in title:
                            n = News(title=article['article_title'], pub=article['article_pub_date'],
                                    text=article['article_text'],
                                    lang=article['article_lang'], source=article['article_source'],
                                    comment=article['article_comment'],
                                    add_date=datetime.datetime.now())
                            print(n.title,"was added....")
                            file.writelines(n.title+"was added at "+ str(datetime.datetime.now())+"\n")
                            n.save()
        except:
            print("Error on ",item)
        continue
        
    print("news collection finished at ",datetime.datetime.now())
    file.writelines("news collection finished at "+str(datetime.datetime.now())+"\n")


def get_baidu_and_save():
    print("start get BaiduNews...,now is ", datetime.datetime.now())
    file.writelines("start get BaiduNews...,now is "+ str(datetime.datetime.now())+"\n")
    result = collect_baidu_news()
    today = datetime.datetime.today().date()
    data_saved = SearchNews.select().where(SearchNews.pub_date == today)
    title = []

    if data_saved.__len__() != 0:
        for news in data_saved:
            title.append(news.title)

    for item in result:
        if item['title'] not in title:
            baidu = SearchNews(
                title=item['title'],
                link=item['href'],
                pub_date=item['pub_date'],
                source=item['source'],
                add_date=datetime.datetime.now()
            )
            print(item['title'], "is added......",", comes from:",item['source'])
            file.writelines(item['title']+" was added at "+ str(datetime.datetime.now())+", comes from "+item['source']+"\n")
            baidu.save()
    print("get baidu.com news finished, now is ", datetime.datetime.now())
    file.writelines("get baidu.com news finished, now is "+ str(datetime.datetime.now())+"\n")


if __name__ == '__main__':
    get_and_save_news()
    get_baidu_and_save()
    #translate()
    db.close()
    file.close()

