from django.db import models

# Create your models here.

class Category(models.Model):
	header_label = models.CharField(max_length=200);

class Link(models.Model):
	category= models.ForeignKey(Category);
	link_label = models.CharField(max_length=200);
	link_url = models.URLField(max_length=200);