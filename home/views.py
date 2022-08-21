from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import product,contact,Catogery
# Create your views here.

def homepage(request):
    post = None
    catogeries = Catogery.get_all_catogeries()
    catogeryID = request.GET.get('catogery')
    if catogeryID:
        post = product.get_all_products_by_ID(catogeryID)
    else:
        post= product.objects.all()
    context={'post':post, 'product':product, 'catogeries':catogeries}
    return  render(request,'home.html', context)
def contacts(request):
    p = contact.objects.all()    
    if request.method=='POST':
         name = request.POST.get('name')
         email = request.POST.get('email')
         message = request.POST.get('message')
         contacts= contact(name=name,email=email, message=message)
        
         contacts.save()

    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')  

def blog(request):
    return render(request,'blog.html')  

def products(request):
    post = None
    catogeries = Catogery.get_all_catogeries()
    catogeryID = request.GET.get('catogery')
    if catogeryID:
        post = product.get_all_products_by_ID(catogeryID)
    else:
        post= product.objects.all()
    context={'post':post, 'product':product, 'catogeries':catogeries}
    return  render(request,'product.html', context)

def detail(request,slug):
    items = product.objects.filter(slug=slug).last()
    context = {'items':items}
    return render(request,'productdetail.html',context)    

def addprod(request):
    #prod= product.objects.all()
    cat=Catogery.objects.all()
    if request.method=="POST":
        prod = product()
        prod.title = request.POST.get('title')
        prod.image = request.FILES['image']
        prod.catogery = Catogery.objects.get(name=request.POST['name'])
        prod.desc = request.POST.get('desc')
        prod.price = request.POST.get('price')
        #addprod = product(title=prod.title,desc=prod.desc,price=prod.price,catogery=prod.catogery,image=prod.image)
        prod.save()  
    return render(request,'add-product.html')    

def deleteprod(request,pk):
    item = product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('admin-dash')
    context={'item':item} 
    return render(request, 'deleteprod.html', context)   


def admindash(request):
    cards = product.objects.all()
    context = {'product':product, 'cards':cards}
    return render(request,'admin-dash.html', context)

