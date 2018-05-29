from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$',views.index,),
    url(r'^register/$', views.register,name='reg'),
    #有名分组
    url(r'^article/(?P<year>\d{4})/(?P<month>\d{2})/$',views.article_year_month),
    # 无名分组
    url(r'^article/(\d{4})/(\d{2})/(\d{2})/$',views.article_year_month_day),

]