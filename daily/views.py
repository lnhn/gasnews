from django.shortcuts import render
import datetime

# Create your views here.

from .get_daily.daily import get_daily_news

def daily_viwe(request):
    news,dic,his=get_daily_news()
    year_=datetime.datetime.today().year
    month_=datetime.datetime.today().month
    day_=datetime.datetime.today().day
    print(year_)
    return render(request,'daily.html',{'news':news,'dic':dic,'his':his,'year':year_,'month':month_,'day':day_})