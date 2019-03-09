from bs4 import BeautifulSoup as bs
from urllib import request as req
import urllib
import datetime


def get_html(url):
    #获得网页的函数
    #print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    page=urllib.request.Request(url,headers=headers)


    try:
        response = urllib.request.urlopen(page)
    except urllib.error.HTTPError as e:
        print(e.code)

    return response.read()


def get_news(content, tag, class_):
    # 获得bs对象
    bs_obj = bs(content, "lxml")
    content_list = bs_obj.find_all(tag, class_=class_)
    return content_list


def filter_news_today(story,date_format,start,end_num,lang):
    # 从中筛选出最新的新闻，今天或者昨天的新闻
    # today=datetime.datetime.strptime("2019-02-21","%Y-%m-%d")
    today = datetime.datetime.today().date()
    yesterday = today + datetime.timedelta(days=-1)

    for index, value in enumerate(story):
        pub_date = datetime.datetime.strptime(value['pub'][start:end_num], date_format).date()
        value['pub']=pub_date
        if lang=="en":
            if pub_date != yesterday:
                story[index] = None
        else:
            if pub_date != today:
                story[index] = None

    story = [item for item in story if not item == None]
    return story


#此方法用于获得文章详细内容后的文章内容提取

def get_articles(story,tag,class_,source,lang):
    #传入数组
    # 获取新闻首页的内容详情
    # tag：新闻清单的标号
    # class_：新闻详情的类别
    # source是从哪里获得的
    # 语言是英文还是中文，是否需要翻译


    articles = []
    for item in story:
        content_detail = get_html(item['href'])
        article = get_news(content_detail, tag, class_) #"articleContent"
        if article.__len__()!=0:
            articles.append(
                {
                    'article_title': item['title'],
                    'article_pub_date': item['pub'],
                    'article_source': item['href'],
                    'article_text': article[0],
                    'article_comment': source,#gasworld
                    'article_lang': lang,#en
                }
            )

    return articles



def get_news_list(url,pages,tag,class_):
    #获取新闻首页的内容的清单，包括了所有的页面的新闻概述
    # tag：新闻清单的标号
    # class_：新闻清单的类别
    #pages:要获得几页

    web_base = url
    web_sites = []
    content_list=[]
    if pages != 0:
        for i in range(pages):
            web_sites.append(web_base + str(i + 1))
        for web in web_sites:
            html_str = get_html(web)
            content_list=content_list+get_news(html_str, tag, class_)
        return content_list
    else:
        web_sites.append(url)
        for web in web_sites:
            html_str = get_html(web)
            content_list=get_news(html_str, tag, class_)
        return content_list
