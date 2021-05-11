
from django.urls import path,re_path
from . import views
# from django.contrib.staticfiles.urls 
# import staticfiles.urlpatterns urlpatterns += staticfile_urlpatterns()


urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('today/',views.news_of_day,name='newsToday'),
re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews')
   
]
#  path('archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews')

