import datetime
from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from django.urls import reverse
from read_statistics.utils import get_seveen_days_read_data
from blog.models import Blog

def get_seven_days_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects \
                .filter(read_details__date__lt=today,read_details__date__gte=date) \
                .values('id','title') \
                .annotate(read_num_sum = Sum('read_details__read_num')) \
                .order_by('-read_num_sum')
    return blogs[:7]

def get_today_hot_data():
    today = timezone.now().date()
    blogs = Blog.objects \
                .filter(read_details__date=today) \
                .values('id','title') \
                .annotate(read_num_sum = Sum('read_details__read_num')) \
                .order_by('-read_num_sum')
    return blogs[:3]

def get_yesterday_hot_day():
    today = timezone.now().date()
    yesterday = today - datetime.timedelta(days=1)
    blogs = Blog.objects \
                .filter(read_details__date=yesterday) \
                .values('id','title') \
                .annotate(read_num_sum = Sum('read_details__read_num')) \
                .order_by('-read_num_sum')
    return blogs[:3]

def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates,read_nums = get_seveen_days_read_data(blog_content_type)
    
    #获取7天热门博客的缓存数据
    hot_blogs_for_7_days = cache.get('hot_blogs_for_7_days')
    if hot_blogs_for_7_days is None:
        hot_blogs_for_7_days = get_seven_days_hot_blogs()
        cache.set('hot_blogs_for_7_days',hot_blogs_for_7_days,3600)

    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['today_hot_data'] = get_today_hot_data()
    context['yesterday_hot_day'] = get_yesterday_hot_day()
    context['seven_days_hot_blogs'] = get_seven_days_hot_blogs()
    return render(request,'home.html', context)

