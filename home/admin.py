from django.contrib import admin
from home.models import Contact
from home.models import Product
# from home.models import Users

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')  # show category in list
    list_filter = ('category',)  # filter by category

# Register your models here.
admin.site.register(Contact)
# admin.site.register(Product)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Users)

# admin pannel
#WhiteMoon  Tenzindakar65@