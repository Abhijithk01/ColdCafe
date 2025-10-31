"""
URL configuration for newproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from cafe.views import home,menus,menu,addmenu,addproductprocess,delete,updateproducts,addupdateproducts,buynow,buynowprocess,car,ordernow,addordernowprocess,delete,addpost,payment_success,payfail,loginp,registernow,registernowprocess,loginprocess
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('',loginp),
    path('loginp/',loginprocess),
    path('registernow/',registernow),
    path('registernow/submit/',registernowprocess),
    path('products/', menus),
    path('products/menu/<int:id>/', menu),
    path('products/menu/<int:id>/delete/',delete),  
    path('addmenu/', addmenu),
    path('addmenu/addproductprocess/',addproductprocess),
    path('products/menu/<int:id>/update/', updateproducts),
    path('products/menu/<int:id>/update/addupdateproducts/', addupdateproducts),
    path('<int:id>/buynow/', buynow),
    path('<int:id>/buynow/buynowprocess/', buynowprocess),
    path('cart/', car),
    path('ordernow/', ordernow),
    path('ordernow/addordernowprocess/', addordernowprocess),
    path('cart/<int:id>/delete/', delete),
    path('addpost/', addpost),
    path('purchased/<str:razorpay_payment_id>/<str:razorpay_order_id>/',payment_success),
    path('payfail/',payfail),


]

    




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)