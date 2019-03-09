from urllib.request import quote, unquote
from gasnews.data import *

# 从百度新闻中爬每天的新闻
key_words = ['氢气', '氢', '氧气', '氧', '氮气', '氮', '氩', '氩气', '氦', '氦', '二氧化碳', '稀有气体', '工业气体', '气体', '林德', '液化空气',
             '特气', '普莱克斯', '空气化工产品', '大阳日酸', '岩谷气体', '杭氧', '空分','LNG','液化天然气','煤气化','盈德','空分','空气分离']


def collect_baidu_news():
    web_list = []
    story = []

    #http://news.baidu.com/ns?word=%E6%B0%A2&tn=news&from=news&cl=2&rn=20&ct=1

    for word in key_words:
        for i in range(1):
            web_list.append(quote('http://news.baidu.com/ns?word=' + word + '&pn='+str(i*10)+'&cl=2&ct=1&tn=news&ie=utf-8&bt=0&et=0', safe=";/?:@&=+$,", encoding="utf-8"))

            #web_list.append(quote('http://news.baidu.com/ns?word=' + word + '&bs=%D1%F5%C6%F8&sr=0&cl=2&rn=' + str(
            #    i * 20) + '&tn=news&ct=0&clk=sortbytime', safe=";/?:@&=+$,", encoding="utf-8"))

    for web in web_list:
        try:
            content = get_html(web).decode()
            news_list = get_news(content, tag="div", class_="result")

            # 需要找到相关的时间，所以要再重新用bs解析一次

            for con in news_list:
                con_bs = bs(str(con), 'lxml')
                date_str = con_bs.find_all(name="p", class_="c-author")[0].text

                if "分钟" in date_str or "小时" in date_str:
                    # print(date_str.replace(" ","").strip())
                    # print(con.h3.a.text.replace("\n","").strip())
                    pub_date = datetime.datetime.today().date()

                else:
                    pub_date = (date_str[date_str.find("年") - 4:date_str.find("年") + 10].replace("年", '-').replace("月",
                                                                                                                   "-").replace(
                        "日", "-"))[:10]
                    pub_date = datetime.datetime.strptime(pub_date, "%Y-%m-%d").date()

                if pub_date == datetime.datetime.today().date():

                    story.append({
                        'title': con.h3.a.text.replace("\n", "").strip(),
                        'pub_date': pub_date,
                        'href': con.h3.a['href'],
                        'source':unquote(web[web.find("?word") + 6:web.find("&pn")])
                    }
                    )
                    #print(unquote(web[web.find("?word") + 6:web.find("&pn")]), "---", story[-1]['pub_date'],
                          #story[-1]['title'])
                    #print(story[-1]['href'])

        except:
            pass
            print("ERROR","on the web ",con.h3.a.text.replace("\n", "").strip(),"the link is:",con.h3.a['href'])
        continue

    return story


# 从中化新网爬新闻

def collect_ccin_news_2():
    story=[]
    web = "http://www.ccin.com.cn/c/search_news?keyword="
    for word in key_words:
        try:
            url=quote(web+word,safe=";/?:@&=+$,", encoding="utf-8")
            html=get_html(url)
            news_list=get_news(html,"div","news-bd")
            for con in news_list:

                pub_date=con.div.text.strip()[:10]
                pub_date=datetime.datetime.strptime(pub_date,"%Y-%m-%d").date()
                if pub_date==datetime.datetime.today().date():
                    story.append({
                        'title':con.h2.a.text ,
                        'pub': con.div.text.strip()[:10],
                        'href': "http://www.ccin.com.cn"+con.h2.a['href'],
                        'source':web,
                    })

                    print(word,story[-1]['pub'],story[-1]['title'])
        except:
            pass
        continue



    news_detail=get_articles(story,tag="div",class_="news-content",source="中化新网",lang="zh")
    return news_detail





