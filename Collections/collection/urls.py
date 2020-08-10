from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from collection import views
app_name='collection'
urlpatterns=[
    path('',views.index,name='index'),
    path('collection-detail/<int:pk>/',views.collectionDetailView,name='collection_detail'),
    path('collection-create/',views.collectionCreateView,name='collection_create'),
    path('collection-update/<int:pk>/',views.collectionUpdateView,name='collection_update'),
    path('collection-delete/<int:pk>/',views.collectionDeleteView,name='collection_delete'),
    path('<int:collection_id>/item-detail/<int:pk>/',views.itemDetailView,name='item_detail'),
    path('<int:collection_id>/item-create/',views.itemCreateView,name='item_create'),
    path('<int:collection_id>/item-update/<int:pk>/',views.itemUpdateView,name='item_update'),
    path('<int:collection_id>/item-delete/<int:pk>/',views.itemDeleteView,name='item_delete'),
    path('collection-search/',views.collectionSearchView,name="collection_search"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
