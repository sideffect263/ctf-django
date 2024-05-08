from django.contrib import admin
from .models import Product ,Order
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    def change_catagory_default(self,request,queryset):
        queryset.update(category="default")
    change_catagory_default.short_description='default category'
    list_display=('title','price','discount','description','category','image')
    search_fields=('title','description','category')
    actions = ('change_catagory_default',)
    list_editable=('price',)


admin.site.register(Product,ProductAdmin)
admin.site.register(Order)