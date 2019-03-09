from gasnews.data import *
from urllib.request import quote,unquote


#  获取gasworld的新闻
def collect_gasworld_news():
    story = []
    # 定义函数中的变量
    web_base = 'https://www.gasworld.com/7356.more?cmd=GoToPage&val='
    pages = 2
    list_tag = "div"
    list_class = "storyDetails"

    content_list = get_news_list(web_base, pages, list_tag, list_class)
    for con in content_list:
        if con.p.span!=None:
            story.append({"title": con.h3.a.text,
                        "pub": con.p.span.text,
                        "href": con.h3.a['href'],
                        })

    filter_story = filter_news_today(story,"%Y-%m-%d",0,10,'en')
    # 获得每一个故事里面的详细内容
    # 定义函数中的变量
    article_tag = "div"
    article_class = "articleContent"
    article_source = "gasworld"
    article_lang = "en"
    return get_articles(filter_story, article_tag, article_class, article_source, article_lang)



def collect_cnpgn_news():
    story = []
    # 定义函数中的变量
    cnpgn_webs=['http://www.cnpgn.com/news/list.php?catid=558&page=',
            'http://www.cnpgn.com/news/list.php?catid=563&page=']

    for web_base in cnpgn_webs:
        pages = 1
        list_tag = "li"
        list_class = "catlist_li"

        content_list = get_news_list(web_base, pages, list_tag, list_class)
        for con in content_list:
            story.append({"title": con.a.text,
                          "pub": con.span.text,
                          "href": con.a['href'],
                          })

    filter_story = filter_news_today(story,"%Y-%m-%d",0,10,'zh')
    # 获得每一个故事里面的详细内容
    # 定义函数中的变量
    article_tag = "div"
    article_class = "content"
    article_source = "气体分离"
    article_lang = "zh"
    return get_articles(filter_story, article_tag, article_class, article_source, article_lang)

#特气123新闻

def collect_teqi123_news():
    #from bs4 import BeautifulSoup as bs
    story = []
    # 定义函数中的变量
    teqi123 = ["http://teqi123.com/news.php?sort=4&page=",
               "http://teqi123.com/news.php?sort=6&page="]

    for web_base in teqi123:
        pages = 1
        list_tag = "div"
        list_class = "main_lm_t"

        content_list = get_news_list(web_base, pages, list_tag, list_class)
        for con in content_list:
            bs_teqi=bs(str(con),'lxml')
            pub_date=bs_teqi.find_all("span")[0].text
            story.append({"title": con.div.a.text,
                          "pub": pub_date,
                          "href": "http://www.teqi123.com"+con.div.a['href'],
                          })

    filter_story = filter_news_today(story,"%Y-%m-%d",1,11,'zh')
    # 获得每一个故事里面的详细内容
    # 定义函数中的变量
    article_tag = "div"
    article_class = "anything"
    article_source = "特气网"
    article_lang = "zh"
    return get_articles(filter_story, article_tag, article_class, article_source, article_lang)


#中国化工报相关的内容

def collect_ccin_news():
    web_base="http://www.ccin.com.cn/c/index"
    story = []
    # 定义函数中的变量
    pages = 0
    list_tag = "div"
    list_class = "news-bd"

    content_list = get_news_list(web_base, pages, list_tag, list_class)
    for con in content_list:
        pub=con.div.text
        start=pub.find(str(datetime.datetime.today().year))
        if start!=-1:
            pub=pub[start:10]
            story.append({"title": con.h2.a.text,
                          "pub": pub,
                          "href": "http://www.ccin.com.cn"+con.h2.a['href'],
                          })
        else:
            continue


    filter_story = filter_news_today(story,"%Y-%m-%d",0,10,'zh')
    # 获得每一个故事里面的详细内容
    # 定义函数中的变量
    article_tag = "div"
    article_class = "news-content-txt"
    article_source = "中国化工报"
    article_lang = "zh"
    return get_articles(filter_story, article_tag, article_class, article_source, article_lang)



def collect_AP_news():
    web_base="http://www.airproducts.com/Company/news-center.aspx"
    story = []
    # 定义函数中的变量
    pages = 0
    list_tag = "li"
    list_class = "press_release"

    content_list = get_news_list(web_base, pages, list_tag, list_class)
    for con in content_list:
        pub_date=datetime.datetime.strptime(str(con.span.text).strip(),"%d %B %Y")
        pub_date=pub_date.strftime("%Y-%m-%d")
        story.append({"title": con.text,
                      "pub": pub_date,
                      "href": "http://www.airproducts.com" + con.a['href'],
                      })

    filter_story = filter_news_today(story, "%Y-%m-%d", 0, 10,'en')
    if filter_story.__len__()!=0:
        #print(filter_story.__len__())
        # 获得每一个故事里面的详细内容
        # 定义函数中的变量
        article_tag = "div"
        article_class = "text_content"
        article_source = "AirProducts"
        article_lang = "en"
        return get_articles(filter_story, article_tag, article_class, article_source, article_lang)
    else:
        return None

def collect_praxair_news():
    web_base="https://www.praxair.com/news?s={%22k%22:%22%22,%22p%22:0,%22ps%22:10}"
    story = []
    # 定义函数中的变量
    pages = 0
    list_tag = "div"
    list_class = "news-item"

    content_list = get_news_list(web_base, pages, list_tag, list_class)
    for con in content_list:
        pub_date=datetime.datetime.strptime(str(con.h5.text).strip(),"%B %d, %Y")
        pub_date=pub_date.strftime("%Y-%m-%d")
        story.append({"title": con.h2.a.text,
                      "pub": pub_date,
                      "href": con.h2.a['href'],
                      })

    filter_story = filter_news_today(story, "%Y-%m-%d", 0, 10,'en')
    # 获得每一个故事里面的详细内容
    # 定义函数中的变量
    if filter_story.__len__() != 0:
        article_tag = "div"
        article_class = "copy"
        article_source = "Praxair"
        article_lang = "en"
        return get_articles(filter_story, article_tag, article_class, article_source, article_lang)
    else:
        return None


#Air Liquide 的新闻和Press

def collect_AL_news():
    web_base="https://en.media.airliquide.com/news/?page="
    story = []
    # 定义函数中的变量
    pages = 2
    list_tag = "div"
    list_class = "card card--topic card--default"

    content_list = get_news_list(web_base, pages, list_tag, list_class)
    for con in content_list:
        pub_date=datetime.datetime.strptime(str(con.div.p.span.text).strip(),"%B %d, %Y")
        pub_date=pub_date.strftime("%Y-%m-%d")

        story.append({"title": con.div.h3.a.text,
                      "pub": pub_date,
                      "href": 'https:'+ con.div.h3.a['href'],
                      })

    filter_story = filter_news_today(story, "%Y-%m-%d", 0, 10,'en')
    # 获得每一个故事里面的详细内容
    # 定义函数中的变量
    if filter_story.__len__() != 0:
        article_tag = "div"
        article_class = "content-text js-publication-responsive"
        article_source = "AirLiquide"
        article_lang = "en"
        return get_articles(filter_story, article_tag, article_class, article_source, article_lang)
    else:
        return None


def collect_linde_news():

    web_base="https://www.linde.com/en/news-media"
    story = []
    # 定义函数中的变量

    html_content=get_html(web_base)
    content_bs=bs(html_content,'lxml')
    content_list=content_bs.find_all("article")
    for con in content_list:
        pub_date = datetime.datetime.strptime(str(con.p.text).strip(), "%m/%d/%Y")
        pub_date = pub_date.strftime("%Y-%m-%d")

        #print(pub_date, con.h3.a.text, con.h3.a['href'])

        story.append({"title": con.h3.a.text,
                      "pub": pub_date,
                      "href": con.h3.a['href'],
                      })

    filter_story = filter_news_today(story, "%Y-%m-%d", 0, 10,'en')
    # 获得每一个故事里面的详细内容
    # 定义函数中的变量
    if filter_story.__len__() != 0:
        article_tag = "div"
        article_class = "list-container"
        article_source = "lindePlc"
        article_lang = "en"
        return get_articles(filter_story, article_tag, article_class, article_source, article_lang)
    else:
        return None

def collect_linde_healthcare_and_engineering_news():
    web_bases=["http://www.linde-healthcare.com/en/news_and_media/press_releases/index.html",
              "https://www.linde-engineering.com/en/news_and_media/press_releases/index.html"]

    story = []
    # 定义函数中的变量

    for web_base in web_bases:
        web_id=web_base[:web_base.find("/en/")]
        html_content=get_html(web_base)
        content_bs=bs(html_content,'lxml')
        content_list=content_bs.find_all("div",class_="item")
        for con in content_list:
            text=con.dt.a.text.strip()
            pub_date = datetime.datetime.strptime(text[:10], "%d.%m.%Y")
            pub_date = pub_date.strftime("%Y-%m-%d")
            title=con.dt.a.text.strip()
            title=title[title.find("/",14)+1:]

            #print(pub_date, con.h3.a.text, con.h3.a['href'])

            story.append({"title": title,
                          "pub": pub_date,
                          "href": web_id + con.dt.a['href'],
                          })

    filter_story = filter_news_today(story, "%Y-%m-%d", 0, 10,'en')
    # 获得每一个故事里面的详细内容
    # 定义函数中的变量
    if filter_story.__len__() != 0:
        article_tag = "article"
        article_class = "component GeneralContent"
        article_source = web_base[web_base.find("linde"):web_base.find(".com")]
        article_lang = "en"
        return get_articles(filter_story, article_tag, article_class, article_source, article_lang)
    else:
        return None






# 中国氢能源网

def collect_china_hydrogen_news():
    web_base="http://www.china-hydrogen.org/"
    story = []
    # 定义函数中的变量
    pages = 0
    list_tag = "div"
    list_class = "news-bd"
    html_content=get_html(web_base)
    content_bs=bs(html_content,"lxml")
    content_ul=str(content_bs.find_all("div",class_="block_2 w440 fl mr10")[0])
    content_list=bs(content_ul,"lxml").find_all("li")
    for con in content_list:

        story.append({"title": con.a.text,
                      "pub": "2019-"+con.span.text,
                      "href": "http://www.china-hydrogen.org"+con.a['href'],
                      })


    filter_story = filter_news_today(story,"%Y-%m-%d",0,10,'zh')
    # 获得每一个故事里面的详细内容
    # 定义函数中的变量

    article_tag = "div"
    article_class = "iart_content"
    article_source = "中国氢能源网"
    article_lang = "zh"
    return get_articles(filter_story, article_tag, article_class, article_source, article_lang)




# Itm Power
#web="http://www.itm-power.com/news-media/news"

# Ballard

#web="http://www.ballard.com/about-ballard/newsroom/news-releases"



