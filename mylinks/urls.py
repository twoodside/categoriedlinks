from django.conf.urls import patterns, url;

from mylinks import views;

urlpatterns = patterns( "",
	# url(r'^$', views.index, name='categoriedlinks_index'),
	url(r'^place/$', views.index, name='categoriedlinks_index'),
	url(r'^update/(?P<stuff>\d+)/$',views.updateNum,name='updateNum'),
	url(r'^update/$',views.update,name='categoriesAddUpdateNum'), 
	url(r'^update/add/(?P<stuff>.+)/$',views.categoriesAddUpdateNum,name='categoriesAddUpdateNum'),
	url(r'^update/add/$',views.categoriesAddUpdate,name='categoriesAddUpdate'),
);