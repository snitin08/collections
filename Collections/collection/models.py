from django.db import models
from django.urls import reverse
from django import forms
# Create your models here.
class CollectionModel(models.Model):
    name = models.CharField(max_length=50)
    def get_absolute_url(self):
        return reverse("collection:collection_detail", kwargs={"pk": self.pk})

class CollectionItemModel(models.Model):
    collecttion_name = models.ForeignKey('CollectionModel',on_delete=models.CASCADE,related_name="items")
    item_name = models.CharField(max_length=100)
    item_url = models.URLField()
    item_image = models.ImageField(upload_to='photos/',blank=True, null=True)