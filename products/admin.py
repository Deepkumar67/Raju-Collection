from django.contrib import admin
from .models import Product,Advertisement

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','title','shop','brand','price','out_of_stock','is_new_arrival','size')
    list_display_links = ('id','title')
    list_filter = ('shop','price','out_of_stock','is_new_arrival','price','brand')
    search_fields = ('title','description','price')

admin.site.register(Product,ProductsAdmin),

class AdvertisementAdmin(admin.ModelAdmin):
	list_display = ('id', 'advertisement_title', 'shop')
	list_filter = ('shop','advertisement_title')
	search_fields = ('advertisement_title', 'shop')
admin.site.register(Advertisement,AdvertisementAdmin)
