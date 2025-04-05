from django import forms
from suppliers.models import Supplier


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'description']
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), 

        }
        labels = {
            
            'name': 'Nome',
            'description': 'Descrição',
        }