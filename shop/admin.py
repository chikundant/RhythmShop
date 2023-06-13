from django.contrib import admin
from .models import CategoryModel, ProductModel
from ckeditor.widgets import CKEditorWidget
from django import forms


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(ProductModel, ProductAdmin)
