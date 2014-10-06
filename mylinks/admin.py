from django.contrib import admin;
from mylinks.models import Category,Link;

# Register your models here.

class LinksInline(admin.StackedInline):
	model=Link;
	extra=3;

class CategoryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,	{'fields':['header_label']}),
	];
	inlines = [LinksInline];
	list_display = ('header_label',);
	
	
admin.site.register(Category,CategoryAdmin);
