from django import forms
from .models import OrderModel


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['first_name', 'last_name', 'email', 'address', 'city']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'appearance-none border-1 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500'}),
            'last_name': forms.TextInput(attrs={'class': 'appearance-none border-1 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500'}),
            'email': forms.TextInput(attrs={'class': 'appearance-none border-1 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500'}),
            'city': forms.TextInput(attrs={'class': 'appearance-none border-1 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500'}),
            'address': forms.TextInput(attrs={'class': 'appearance-none border-1 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500'}),
        }
