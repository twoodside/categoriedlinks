from django.conf.urls import patterns, url;

from mylinks import views;

urlpatterns = patterns( "",
	url(r'^$', views.index, name='categoriedlinks_index'),
	
	url(r'^update/$',views.update,name='update'), 
	url(r'^update/add/$',views.categoriesAddUpdate,name='categoriesAddUpdate'),
	
	url(r'^update/(?P<stuff>\d+)/$',views.updateNum,name='updateNum'),
	url(r'^update/add/(?P<stuff>.+)/$',views.categoriesAddUpdateNum,name='categoriesAddUpdateNum'),
);