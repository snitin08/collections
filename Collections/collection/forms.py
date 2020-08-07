from django import forms  
from collection.models import CollectionModel,CollectionItemModel

class CollectionModelForm(forms.ModelForm):
    class Meta:  
        model = CollectionModel  
        fields = "__all__"  

class CollectionItemModelForm(forms.ModelForm):
    class Meta:  
        model = CollectionItemModel 
        fields =  ('item_name','item_url','item_image')