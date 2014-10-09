import datetime;
import re;
from django.shortcuts import render;
from django.http import HttpResponse,HttpResponseRedirect;
from django.template import RequestContext, loader;
from django.core.urlresolvers import reverse;
from django.shortcuts import redirect;

from mylinks.models import Category,Link;

# Create your views here.
def index(request):
	categories = Category.objects.order_by('-header_label');
	template = loader.get_template('mylinks/index.html');
	context = RequestContext(request, {
		'categories' : categories,
	});
	m=reverse("mylinks:categoriedlinks_index");
	return HttpResponse( template.render(context) );


def update(request):
	categories = Category.objects.order_by('-header_label');
	#links = Link.objects.order_by('');
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
	# return HttpResponse( "Object id \"%s\"."%(stuff) );


def categoriesAddUpdate(request):
	
	
	
	return HttpResponse("HelloWorld");


def categoriesAddUpdateNum(request,stuff):
	
	p=Category.objects.get(id=stuff);
	
	r=request.POST["maxId"]+" ";
	
	n=int(request.POST["maxId"])+1;
	r+=str(n)+"<br>";
	newLinks=[0]*n;
	for i in range(0,n):
		newLinks[i]=["",""];
	
	#r+=newLinks+"<br>";
	
	for x in request.POST:
		# r+=x+" "+request.POST[x]+"<br>";
		try:
			linktype,linkid=x.split("_",1);
		except ValueError:
			continue;
		
		if (linktype=="Link"):
			newLinks[int(linkid)][0]=request.POST[x];
		elif (linktype=="URL"):
			newLinks[int(linkid)][1]=request.POST[x];
		
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
	m=reverse("mylinks:categoriedlinks_index");
	#m=reverse(index);
	return HttpResponse( "dsa" );
	#return HttpResponse( reverse("categoriesAddUpdateNum") );
	#return index(request);
	#return redirect("categoriedlinks-index");