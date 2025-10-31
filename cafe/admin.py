from django.contrib import admin

# Register your models here.
from cafe. models import Products,Cart,Post,Ordernow

class ProductsAdmin(admin.ModelAdmin):
    list_display=["id","pitem","pname","prate","pqty"]


class CartAdmin(admin.ModelAdmin):
    list_display=["id","pitem","pname","prate","pqty","quandity","total","name"]

class Postadmin(admin.ModelAdmin):
    list_display=["id","title","body","slug","date","banner"]




class Orderadmin(admin.ModelAdmin):
    list_display=["firstname","lastname","address","streetaddress","mobilenumber","email","totalvalue","razorpay_order_id","razorpay_payment_id","paid","date"]
    list_filter = ['date']
    search_fields = ['firstname','lastname','address','mobilenumber','email','totalvalue','razorpay_order_id']
    date_hierarchy = 'date'




admin.site.register(Products,ProductsAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(Post,Postadmin)
admin.site.register(Ordernow,Orderadmin)

