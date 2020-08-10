from django.shortcuts import render, redirect, get_object_or_404
from collection.models import CollectionModel, CollectionItemModel
from .forms import CollectionItemModelForm, CollectionModelForm
from django.conf import settings
# Create your views here.
def index(request):
    collection_list = CollectionModel.objects.all()

    return render(request,"collection/index.html",{"collection_list":collection_list})

def collectionDetailView(request,pk):
    collection = CollectionModel.objects.get(pk=pk)
    collection_items = collection.items.all()
    return render(request,"collection/collection_detail.html",
        {
            "collection":collection,
            "collection_items":collection_items,
        }
    )

def collectionSearchView(request):
    method_dict = request.GET
    query = method_dict.get('q', None) # method_dict['q']
    print(query is '')
    if query is not None:
        collection_list = CollectionModel.objects.filter(name__icontains=query)
        return render(request,"collection/collection_search.html",{"collection_list":collection_list})
    return render(request,"collection/collection_search.html",{"collection_list":None})

def collectionCreateView(request):
    if request.method == "POST":
        form = CollectionModelForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.save()
            return redirect('collection:index')
    else:
        form = CollectionModelForm()
    return render(request, 'collection/collection_create.html', {'form': form})

def collectionUpdateView(request,pk):
    collection = get_object_or_404(CollectionModel, pk = pk) 
    form = CollectionModelForm(request.POST or None, instance=collection)
    if form.is_valid(): 
        form.save() 
        return redirect('collection:collection_detail',pk=pk)
    return render(request,'collection/collection_create.html',{"form":form}) 

def collectionDeleteView(request,pk):
    obj = get_object_or_404(CollectionModel, pk = pk) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return redirect("collection:index") 
  
    return render(request, "collection/collection_delete.html", {}) 

def itemDetailView(request,pk,collection_id):
    item = CollectionItemModel.objects.get(pk=pk)
    
    return render(request,"collection/item_detail.html",{"item":item,"media_url":settings.MEDIA_URL})
    

def itemCreateView(request,collection_id):
    if request.method == "POST":
        form = CollectionItemModelForm(request.POST, request.FILES or None)
        if form.is_valid():
            
            item = form.save(commit=False)
            item.collecttion_name_id = collection_id
            item.save()
            return redirect('collection:index')
    else:
        form = CollectionItemModelForm()
    return render(request,"collection/item_create.html",{"form":form})


def itemUpdateView(request,pk,collection_id):
    item = get_object_or_404(CollectionItemModel, pk = pk) 
    form = CollectionItemModelForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid(): 
        item = form.save(commit=False)
        item.collecttion_name_id = collection_id
        item.save()
        return redirect('collection:item_detail',pk=pk,collection_id=collection_id)
    return render(request,'collection/item_create.html',{"form":form})

def itemDeleteView(request,pk,collection_id):
    obj = get_object_or_404(CollectionItemModel, pk = pk) 
    
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return redirect("collection:index") 
  
    return render(request, "collection/item_delete.html", {}) 
