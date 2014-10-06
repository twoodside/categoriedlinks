import datetime;
import re;
from django.shortcuts import render;
from django.http import HttpResponse,HttpResponseRedirect;
from django.template import RequestContext, loader;
from django.core.urlresolvers import reverse


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
	
	r=p.header_label;
	
	for x in request.POST:
		print(x);
		try:
			linktype,linkid=x.split("_",1);
		except ValueError:
			continue;
			
		print(linktype,linkid);
		
		if (linktype=="Link" or linktype=="URL"):
			print("2.5");
			if ( p.link_set.filter(id=linkid).exists() ):		
				print("3a");
				link=p.link_set.get(id=linkid);
				if (linktype=="Link"):
					print("4aa");
					if ( link.link_label != request.POST[x] ):
						link.link_label=request.POST[x];
				elif (linktype=="URL"):
					print("4ab");
					if ( link.link_url != request.POST[x] ):
						link.link_url=request.POST[x];
						
				link.save();
			else:
				print("3b");
				link=Link();
				link.category=p;
				if (linktype=="Link"):
					print("4ba");
					link.link_label=request.POST[x];
				elif (linktype=="URL"):
					print("4bb");
					link.link_url=request.POST[x];
				link.save();
		
	
	
	return HttpResponse(r);