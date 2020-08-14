from django import forms  
from collection.models import CollectionModel,CollectionItemModel
from django.forms import modelform_factory
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class CollectionModelForm(forms.ModelForm):
    class Meta:  
        model = CollectionModel  
        fields = ('name',)
        


class CollectionItemModelForm(forms.ModelForm):
    class Meta:  
        model = CollectionItemModel 
        fields =  ('item_name','item_url','item_image')


