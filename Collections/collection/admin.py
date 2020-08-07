from django.contrib import admin
from .models import CollectionItemModel,CollectionModel
# Register your models here.
admin.site.register(CollectionItemModel)
admin.site.register(CollectionModel)
