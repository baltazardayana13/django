from django.contrib import admin
from .models import Category, Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display =('id', 'title')
    fields =('title',)
admin.site.register(Category,CategoryAdmin)
    

class ProductAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'price', 'category')
    #fields =('title',)
    #field solo para un subconjunto, para todos lo quito
admin.site.register(Product,ProductAdmin)
