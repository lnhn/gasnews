from model import *
from bs4 import BeautifulSoup as bs
from google.cloud import translate

client=translate.Client()

def google_translate():

    newslist=News.select().where(News.lang=='en')
    #t = T(service_urls=['translate.google.cn'])
    #client=translate.Client()
    for item in newslist:

        text=item.title
        title=client.translate(text,'zh-cn')['translatedText']
        article=""
        news_bs=bs(item.text,'lxml').find_all('p')
        if news_bs.__len__!=0:
            for sentence in news_bs:
                print(sentence.text)
                try:
                    zh=client.translate(str(sentence.text),'zh-cn')['translatedText']
                    article=article+zh+"\n"
                    print(zh)
                except:
                    pass
                continue
                
            tn=TransNews(
                title=title,
                pub=item.pub,
                text=article,
                source=item.source,
                comment=item.comment )
            tn.save()
            News.update({News.lang:"en-zh"}).where(News.id==item.id).execute()
    db.close()
                


google_translate()