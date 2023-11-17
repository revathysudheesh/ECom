from django.shortcuts import render, redirect
from MyApp.models import CategoryDB, ProductDB
from Frontend.models import UserDB,CartDB, BillingAddressDB
from django.contrib import messages



# Create your views here.
def UserHome(request):
    cat = CategoryDB.objects.all()
    pro=ProductDB.objects.all()
    return render(request, 'home.html', {'cat': cat,'pro':pro})

def Contact(request):
    cat = CategoryDB.objects.all()
    return render(request, 'contact.html', {'cat': cat})

def ProductShop(request):
    cat = CategoryDB.objects.all()
    pro=ProductDB.objects.all()
    return render(request, 'product.html', {'pro':pro, 'cat': cat})

def SingleProduct(request, pro_id):
    products=ProductDB.objects.get(id=pro_id)
    return render(request, 'singleproduct.html', {'products':products})

def CategoryPage(request,cat_name):
    cat = CategoryDB.objects.all()
    pro = ProductDB.objects.filter(CatName=cat_name)
    return render(request, 'category.html', {'cat': cat, 'pro':pro})

def UserRegistration(request):
    return render(request, 'userRegistration.html')

def saveUser(request):
    if request.method=="POST":
        na=request.POST.get("name")
        em=request.POST.get("email")
        mo=request.POST.get("mob")
        pw=request.POST.get("password")
        cpw=request.POST.get("cpassword")
        img=request.FILES['img']
        flag=0
        if UserDB.objects.filter(UserName=na).exists():
            flag=1
        if(flag==0):
            if(pw==cpw):
                obj=UserDB(UserName=na,UserEmail=em, UserContact=mo,UserPassword=pw,Image=img)
                obj.save()
                messages.success(request, "Registration done successfully..!")
                return redirect('UserRegistration')
            else:
                messages.error(request,"Password and Confirm password must be same")
                return redirect('UserRegistration')
        else:
            messages.error(request, "Username already exists ")
            return redirect('UserRegistration')

def user_login(request):
    if request.method=="POST":
        uname=request.POST.get('name')
        pw=request.POST.get('password')
        if UserDB.objects.filter(UserName=uname, UserPassword=pw).exists():
            request.session['UserName']=uname
            request.session['UserPassword']=pw
            messages.success(request, "Logged in successfully..!")
            return redirect(UserHome)
        else:
            return redirect(UserRegistration)
    return redirect(UserRegistration)

def user_logout(request):
   del request.session['UserName']
   del request.session['UserPassword']
   messages.success(request, "Successfully logged out..!")

   return redirect(UserRegistration)

def submitCart(request):
    if request.method=="POST":
        useN=request.POST.get("userName")
        proN=request.POST.get("proName")
        prodes=request.POST.get("proDesc")
        qt = request.POST.get("qty")
        to = request.POST.get("total")
        obj=CartDB(UserName=useN,ProName=proN,Description=prodes, Quantity=qt, TotalPrice=to)
        obj.save()
        messages.success(request, "Item added to the cart..!")

        return redirect('DisplayCart')

def DisplayCart(request):
    cart = CartDB.objects.all()
    cat = CategoryDB.objects.all()
    data=CartDB.objects.filter(UserName=request.session['UserName'])
    total_price = 0
    for i in data:
        total_price = total_price + i.TotalPrice
    return render(request, 'cart.html', {'cart':cart, 'data':data, 'cat':cat, 'total_price':total_price})

def DeleteItem(request, dataid):
   pro=CartDB.objects.filter(id=dataid)
   pro.delete()
   return redirect(DisplayCart)

def ItemCheckout(request):
    cat=CategoryDB.objects.all()
    data = CartDB.objects.filter(UserName=request.session['UserName'])
    total_price = 0
    for i in data:
        total_price = total_price + i.TotalPrice
    return render(request, 'checkout.html', {'cat':cat, 'data':data,  'total_price':total_price})

def SaveBillingAddress(request):
    if request.method=="POST":
        useN = request.POST.get("userName")
        fna=request.POST.get("fname")
        lna=request.POST.get("fname")
        cm=request.POST.get("company")
        co = request.POST.get("contact")
        cy= request.POST.get("country")
        em = request.POST.get("email")
        ad1 = request.POST.get("add1")
        ad2 = request.POST.get("add2")
        ct=request.POST.get("city")
        st=request.POST.get("state")
        pc=request.POST.get("zip")
        com = request.POST.get("comments")
        obj=BillingAddressDB(UserName=useN,BillingFirstName=fna,BillingLastName=lna,BillingCompanyName=cm,BillingMail=em, BillingAddress1=ad1,BillingAddress2=ad2,BillingCity=ct,BillingState=st,BillingContact=co, BillingPincode=pc,BillingComments=com)
        obj.save()
        messages.success(request, "Order placed successfully..!")
        return redirect('ItemCheckout')