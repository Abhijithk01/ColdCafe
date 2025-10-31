from django.shortcuts import render,redirect
from django.template import loader
from django.http import request,HttpResponse,JsonResponse
from cafe. models import Products,Cart,Ordernow,Post
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import razorpay
import json

client = razorpay.Client(auth=("rzp_test_RIwFh5XRXmsLtl","YhsJAEUMvnd4eaqwMRmeZ81E"))


@csrf_exempt


def loginp(request):
    return render(request,"login.html")

def registernow(request):
    return render(request,"register.html")    


# def registernowprocess(request):
#        c=""
#        if request.method=='POST':
#         uname=request.POST['username']
#         # fname=request.POST['fname']
#         # lname=request.POST['lname']
#         email=request.POST['email']
#         pwd=request.POST['psw']
#         rpwd=request.POST['psw-repeat']
#        if(pwd==rpwd):
#             user = User.objects.create_user(uname, email, pwd)    
      
#             return redirect('/')
        
#        else:
#             c=True
#             d={"message":c}
#             return render(request,'register.html',d)


def registernowprocess(request):
        
    if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('psw')
            password2 = request.POST.get('psw-repeat')

            if password1 != password2:
                return render(request, 'register.html', {'error': 'Passwords do not match.Try again'})

            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': 'Username already exists.'})

            # Create user
            user = User.objects.create_user(username=username, email=email, password=password1)
            return redirect('/')  # or your success page

    return render(request, 'register.html')

# def loginprocess(request):
#         c=""
#         username = request.POST["username"]
#         password = request.POST["psw"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/home/')
#         else:
#             c=True
#             d={"message":c}
#             return render(request,"login.html",d)

@csrf_exempt      
def loginprocess(request):
    error_message = None

    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['psw']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/')  
            else:
                error_message = 'Invalid credentials. Please try again.'

            return render(request, 'login.html', {'error_message': error_message})






@login_required(login_url='')
def home(request):
    return render(request,"home.html")


@login_required
def menus(request):
    d=Products.objects.all()
    context={
        "pro":d}
    return render(request,"products.html",context)

    
@login_required
def menu (request,id):
    e=Products.objects.get(id=id)
    context={
        "prod":e}
    return render(request,"menu.html",context)


@login_required
def addmenu(request):
    return render(request,"addmenu.html")

@login_required



def addproductprocess(request):
    if request.method == "POST":
        pitem = request.POST.get('pitem')
        pname = request.POST.get('pname')
        prate = request.POST.get('prate')
        pqty = request.POST.get('pqty')
        img = request.FILES.get('img')  # handles image file upload

        print("Uploaded image:", img)

        # Save product
        p = Products(
            pitem=pitem,
            pname=pname,
            prate=prate,
            pqty=pqty,
            banner=img
        )
        p.save()

        return redirect('/products/')  # redirect to your product list page

    return render(request, 'addproduct.html')


# @csrf_exempt
# def addproductprocess(request):
#     if request.method=="POST":
#         pitem=request.POST['pitem']
#         pname=request.POST['pname']
#         prate=request.POST['prate']
#         pqty=request.POST['pqty']
#         img = request.FILES.get('img')  
#         print(img)
#         p=Products(pitem=pitem,pname=pname,prate=prate,pqty=pqty,banner=img)
#         p.save()

#     return redirect("/products/")

@login_required

def delete(request,id):
    d=Products.objects.get(id=id)
    d.delete()
    return redirect("/products/")


@login_required
def updateproducts(request,id):
    return render(request,"update.html")
    

@login_required


@csrf_exempt
def addupdateproducts(request,id):
    if request.method=="POST":
        pitem=request.POST['pitem']
        pname=request.POST['pname']
        prate=request.POST['prate']
        pqty=request.POST['pqty']
        q=Products.objects.get(id=id)
        q.pitem=pitem
        q.pname=pname
        q.prate=prate
        q.pqty=pqty
        q.save()

        return redirect("/products/")
    

    
@login_required

def buynow(request,id):
        pr=Products.objects.get(id=id)
        co={
            "pr":pr
        }
        return render(request,"buynow.html",co)


@login_required
@csrf_exempt
def buynowprocess(request,id):
    pro=Products.objects.get(id=id)

    if request.method=="POST":
    
       
        quandity=request.POST['quandity']
        tot=int(quandity)*pro.prate
     

        print(tot)
        h=Cart(pitem=pro.pitem,pname=pro.pname,prate=pro.prate,pqty=pro.pqty,quandity=quandity,total=tot,name=request.user)
        h.save()       

        return redirect("/products/")
    

@login_required
def delete(request,id):
    g=Cart.objects.get(id=id)
    g.delete()
    return redirect("/cart/")


@login_required     

def car(request):
    t=Cart.objects.filter(name=request.user)
    print(t)

    context={
        "car":t,
        }
    return render(request,"carts.html",context)

@login_required

def ordernow(request):
    t=Cart.objects.all()

    su=0
    for k in t:

        su=su+k.total
    co={
        "su":su,
        "car":t
    }

    return render(request,"ordernow.html",co)

@csrf_exempt

@login_required
def addordernowprocess(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        address=request.POST['address']
        streetaddress=request.POST['streetaddress']
        mobilenumber=request.POST['mobilenumber']
        email=request.POST['email']
        totalvalue=request.POST['totfull']
        totalv=int(totalvalue)
        
       
        razorpay_order = client.order.create(dict(amount=totalv*100, currency='INR', payment_capture='1'))
        p=Ordernow(firstname=firstname,lastname=lastname,address=address,streetaddress=streetaddress,mobilenumber=mobilenumber,email=email,totalvalue=totalv,razorpay_order_id = razorpay_order['id'])

        p.save()
        context = {
            'order': p,
            'razorpay_key_id': settings.RAZORPAY_KEY_ID,
            'amount': totalv*100,
            'amount2':totalv,
            'razorpay_order_id': razorpay_order['id'],

        }
        print(razorpay_order)
        return render(request, 'placeorder.html',context)




@login_required
# def payment_success(request,razorpay_payment_id,razorpay_order_id):
#     order=Ordernow.objects.get(razorpay_order_id=razorpay_order_id)
#     order.paid=True
#     order.razorpay_payment_id=razorpay_payment_id
#     order.save()
  
  
#     return render(request, 'success.html')

def payment_success(request,razorpay_payment_id,razorpay_order_id):
    order=Ordernow.objects.get(razorpay_order_id=razorpay_order_id)
    order.paid=True
    order.razorpay_payment_id=razorpay_payment_id
    order.save()
    if request.user.is_authenticated:
        cart = Cart.objects.filter(name=request.user)
        if cart:
            cart.delete() 
  
  
    return render(request, 'success.html')



@login_required
def payfail(request):
    return render(request,"payfail.html")

@login_required
def addpost(request):
        add=Post.objects.all()
        co={
            "post":add}
        return render(request,"products2.html",co)

        
                
                


 
 
    
    
    
    
    




    

    

    





# Create your views here.
