import datetime;
import re;
from django.shortcuts import render;
from django.http import HttpResponse,HttpResponseRedirect;
from django.template import RequestContext, loader;
from django.shortcuts import redirect;

from mylinks.models import Category,Link;

# Create your views here.
def index(request):
	categories = Category.objects.order_by('-header_label');
	template = loader.get_template('mylinks/index.html');
	context = RequestContext(request, {
		'categories' : categories,
	});
	return HttpResponse( template.render(context) );


def update(request):
	categories = Category.objects.order_by('-header_label');
	template = loader.get_template('mylinks/update.html');
	context = RequestContext(request, {
		'categories' : categories,
	});
	return HttpResponse( template.render(context) );


def updateNum(request,stuff):
	category = Category.objects.get(id=stuff);
	template = loader.get_template('mylinks/updateNum.html');
	context = RequestContext(request, {
		'category' : category,
	});
	return HttpResponse( template.render(context) );


def categoriesAddUpdate(request):
	
	cats=Category.objects;
	r="";
	
	for x in request.POST:
		try:
			trash,catid=x.split("_",1);
			catid=int(catid);
		except ValueError:
			continue;
			
		if trash!="Cat":
			continue;
		
		if cats.filter(id=catid).exists():
			category=cats.get(id=catid);
		else:
			category=Category();
		category.header_label=request.POST[x];
		category.save();
	
	return redirect("mylinks:categoriedlinks_index");


def categoriesAddUpdateNum(request,stuff):
	
	p=Category.objects.get(id=stuff);
	
	r=request.POST["maxId"]+" ";
	
	n=int(request.POST["maxId"])+1;
	r+=str(n)+"<br>";
	newLinks=[0]*n;
	for i in range(0,n):
		newLinks[i]=["",""];
	
	for x in request.POST:
		try:
			linktype,linkid=x.split("_",1);
		except ValueError:
			continue;
		
		if (linktype=="Link"):
			newLinks[int(linkid)][0]=request.POST[x];
		elif (linktype=="URL"):
			newLinks[int(linkid)][1]=request.POST[x];
		elif (linktype=="Header"):
			if Category.objects.filter( id=int(linkid) ).exists():
				category=Category.objects.get( id=int(linkid) );
			else:
				category=Category();
			category.header_label=request.POST[x];
			category.save();
		
	for i in range( 0,len(newLinks) ):
		if (newLinks[i]!=["",""]):
			if p.link_set.filter( id=str(i) ).exists():
				link=p.link_set.get( id=str(i) );
			else:
				link=Link();
			link.category=p;
			link.link_label=newLinks[i][0];
			link.link_url=newLinks[i][1];
			link.save();
			
	
	
	return redirect("mylinks:categoriedlinks_index");