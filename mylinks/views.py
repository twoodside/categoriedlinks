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
	
	r="";
	
	newLinks=[];
	
	for x in request.POST:
		try:
			linktype,linkid=x.split("_",1);
		except ValueError:
			continue;
			
		
		if (linktype=="Link" or linktype=="URL"):
			if ( p.link_set.filter(id=linkid).exists() ):
				link=p.link_set.get(id=linkid);
				if (linktype=="Link"):
					r+="1 "+request.POST[x]+"\n";
					if ( link.link_label != request.POST[x] ):
						link.link_label=request.POST[x];
				elif (linktype=="URL"):
					r+="2 "+request.POST[x]+"\n";
					if ( link.link_url != request.POST[x] ):
						link.link_url=request.POST[x];
						
				link.save();
			else:
				linkid=int(linkid);
				while ( len(newLinks) <= linkid ):
					newLinks.append('\0');
				if (newLinks[linkid] == '\0'):
					link=Link();
					link.category=p;
					if (linktype=="Link"):
						r+="3 "+request.POST[x]+"\n";
						link.link_label=request.POST[x];
					elif (linktype=="URL"):
						r+="4 "+request.POST[x]+"\n";
						link.link_url=request.POST[x];
					newLinks[linkid]=link;
				else:
					link=newLinks[linkid];
					if (linktype=="Link"):
						r+="5 "+request.POST[x]+"\n";
						link.link_label=request.POST[x];
					elif (linktype=="URL"):
						r+="6 "+request.POST[x]+"\n";
						link.link_url=request.POST[x];
					newLinks[linkid]=link;

	for link in newLinks:
		if (link != '\0'):
			link.save();
	
	return HttpResponse(r);
	#return index(request);