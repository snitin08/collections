from django.shortcuts import render, redirect, get_object_or_404
from collection.models import CollectionModel, CollectionItemModel
from .forms import CollectionItemModelForm, CollectionModelForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.urls import reverse
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        collection_list = CollectionModel.objects.filter(user=request.user)
    else:
        collection_list = {}
    print(request.user)
    return render(request,"collection/index.html",{"collection_list":collection_list})

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('collection:index'))


def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        
        # Check to see both forms are valid
        if user_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
           

            # Now save model
            

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'collection/register.html',
                          {'user_form':user_form,                           
                           'registered':registered})


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'collection/login.html', {})
@login_required
def collectionDetailView(request,pk):
    collection = CollectionModel.objects.get(pk=pk)
    collection_items = collection.items.all()
    return render(request,"collection/collection_detail.html",
        {
            "collection":collection,
            "collection_items":collection_items,
        }
    )
@login_required
def collectionSearchView(request):
    method_dict = request.GET
    query = method_dict.get('q', None) # method_dict['q']
    
    if query is not None:
        #collection_list = CollectionModel.objects.filter(name__icontains=query)
        collection_list = CollectionModel.objects.search(query,request.user.id)
        return render(request,"collection/collection_search.html",{"collection_list":collection_list})
    return render(request,"collection/collection_search.html",{"collection_list":None})

@login_required
def collectionCreateView(request):
    if request.method == "POST":
        form = CollectionModelForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            print(collection)
            collection.user = request.user
            collection.save()
            return redirect('collection:index')
    else:
        form = CollectionModelForm()
    return render(request, 'collection/collection_create.html', {'form': form})

@login_required
def collectionUpdateView(request,pk):
    collection = get_object_or_404(CollectionModel, pk = pk) 
    form = CollectionModelForm(request.POST or None, instance=collection)
    if form.is_valid(): 
        form.save() 
        return redirect('collection:collection_detail',pk=pk)
    return render(request,'collection/collection_create.html',{"form":form}) 

@login_required
def collectionDeleteView(request,pk):
    obj = get_object_or_404(CollectionModel, pk = pk) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return redirect("collection:index") 
  
    return render(request, "collection/collection_delete.html", {}) 

@login_required
def itemDetailView(request,pk,collection_id):
    item = CollectionItemModel.objects.get(pk=pk)
    
    return render(request,"collection/item_detail.html",{"item":item,"media_url":settings.MEDIA_URL})
    

@login_required
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

@login_required
def itemUpdateView(request,pk,collection_id):
    item = get_object_or_404(CollectionItemModel, pk = pk) 
    form = CollectionItemModelForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid(): 
        item = form.save(commit=False)
        item.collecttion_name_id = collection_id
        item.save()
        return redirect('collection:item_detail',pk=pk,collection_id=collection_id)
    return render(request,'collection/item_create.html',{"form":form})

@login_required
def itemDeleteView(request,pk,collection_id):
    obj = get_object_or_404(CollectionItemModel, pk = pk) 
    
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return redirect("collection:index") 
  
    return render(request, "collection/item_delete.html", {}) 
