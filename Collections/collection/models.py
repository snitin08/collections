from django.db import models
from django.urls import reverse
from django.db.models import Q
from django import forms
from django.contrib.auth.models import User
# Create your models here.
class CollectionQuerySet(models.QuerySet):
    
    def search(self, query,user):
        
        lookups = (Q(user=user) &
            (Q(name__icontains=query)|Q(items__item_name__icontains=query))) 
        print(lookups)                  
        return self.filter(lookups).distinct()

class CollectionManager(models.Manager):
    def search(self, query, user):
        return self.get_queryset().search(query, user)

    def get_queryset(self):
        return CollectionQuerySet(self.model, using=self._db)


class CollectionModel(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,related_name='collections')
    name = models.CharField(max_length=50)
    objects = CollectionManager()
    def get_absolute_url(self):
        return reverse("collection:collection_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.name

class CollectionItemModel(models.Model):    
    collecttion_name = models.ForeignKey('CollectionModel',on_delete=models.CASCADE,related_name="items")
    item_name = models.CharField(max_length=100)
    item_url = models.URLField()
    item_image = models.ImageField(upload_to='photos',blank=True, null=True)

    def __str__(self):
        return self.item_name