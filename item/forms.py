from django import forms
from .models import Item 

INPUT_CLASS = 'w-full py-4 px-6 rounded-xl border'
class newItemForm(forms.ModelForm):
    class Meta : 
        model = Item
        fields = ('category', 'name', 'price', 'description', 'item_profile')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASS
            }),

            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
    
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS
            }),
            
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),

            'item_profile': forms.FileInput(attrs={
                'class': INPUT_CLASS
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta : 
        model = Item
        fields = ('name', 'price', 'description', 'item_profile', 'is_sold')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
    
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS
            }),
            
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),

            'item_profile': forms.FileInput(attrs={
                'class': INPUT_CLASS
            }),
        }
