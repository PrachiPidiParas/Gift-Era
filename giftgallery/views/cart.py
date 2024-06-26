from django.shortcuts import render
from giftgallery.models.products import Product
from django.views import View

class Cart(View):
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(ids)
        print(products)

        return render(request,'cart.html',{'product':products})