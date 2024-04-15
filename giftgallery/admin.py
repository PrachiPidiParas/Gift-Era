# from django.contrib import admin

# # Register your models here.

# from .models.products import Product
# # admin.site.register(Product)

# from .models.category import Category
# # admin.site.register(Category)

# from .models.front import Front
# admin.site.register(Front)

# #for the table formate data in admin site 
# class AdminProduct(admin.ModelAdmin):
#     list_display = ['name','price','category']
 
# class AdminCategory(admin.ModelAdmin):
#     list_display=['name']

# admin.site.register(Product,AdminProduct)
# admin.site.register(Category,AdminCategory)

from django.contrib import admin
from .models.products import Product
from .models.category import Category
from .models.customer import Customer
from .models.order import Order
from .models.front import Front

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category','description']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']
# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Front)