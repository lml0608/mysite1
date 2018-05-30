from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^book/$',views.book),
    url(r'^addbook/$',views.addbook),
    url(r'^update/$',views.update),
    url(r'^delete/$',views.delete),
    url(r'^selectbook/$',views.selectbook),

    url(r'^$',views.index),
    url(r'^register/$', views.register,name='reg'),
    #有名分组
    url(r'^article/(?P<year>\d{4})/(?P<month>\d{2})/$',views.article_year_month),
    # 无名分组
    url(r'^article/(\d{4})/(\d{2})/(\d{2})/$',views.article_year_month_day),



    url(r'^duobiao/$',views.duobiao),

    url(r'^addbook2/$', views.addbook2),
    url(r'^update2/$', views.update2),
    url(r'^delete2/$', views.delete2),
    url(r'^selectbook2/$', views.selectbook2),




    url(r'^duoduiduo/$', views.duoduiduo),




]