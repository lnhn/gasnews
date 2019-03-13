import urllib.request
import json

import random

app_key = "1112e262c63493e23660c2ccc27482f9"

def get_daily_news():

        keywords = ["social","caijing", "ai",  "it",
                "vr",  "qiwen", "guonei","health", "world", "travel", "mobile",
                "apple", "startup", "keji",  "tiyu", "huabian",
                  ]

        base_web="http://api.tianapi.com/"

        webs=[base_web+item+"/?key="+app_key+"&num=10" for item in keywords]

        news_list=[]

        for web in webs:
                result=urllib.request.urlopen(web).read().decode()
                result=json.loads(result)
                for news in result['newslist']:
                        news_list.append(news['title'])

        news_result=random.sample(news_list,10)


        eng="http://api.tianapi.com/txapi/ensentence/?key="+app_key

        eng_one=json.loads(urllib.request.urlopen(eng).read().decode())

        eng_one=eng_one["newslist"][0]['en'] +"**"+eng_one["newslist"][0]['zh']

        dics=[]

        dic_web="http://api.tianapi.com/txapi/dictum/?key="+app_key+"&num=5"

        dictum=json.loads(urllib.request.urlopen(dic_web).read().decode())

        for item in dictum['newslist']:
                #print(item)
                dics.append(item['content']+" --"+item['mrname'])

        dictum_news=random.sample(dics,1)


        his=[]

        his_web="http://api.tianapi.com/txapi/lishi/?key="+app_key+"&num=5"

        history=json.loads(urllib.request.urlopen(his_web).read().decode())

        for item in history['newslist']:
                #print(item)
                his.append(item['title']+"  "+item['lsdate'])

        histtory_news=random.sample(his,1)

        news_id=1

        for n in news_result:
                print(news_id,".",n)
                news_id+=1

        print("历史上的今天："+histtory_news[0])
        print("名言:"+dictum_news[0])

        return news_result,histtory_news[0],dictum_news[0]

