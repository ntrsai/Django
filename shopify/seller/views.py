from django.shortcuts import render,redirect
from seller.models import Product  

# Create your views here.
def dashboard(request):
    if(request.user.is_authenticated):
        return render(request, 'seller/dashboard.html')
    else:
        return redirect('/')

def app_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        is_available = 'is_available' in request.POST
           

        created_product = Product.objects.create(
            name=name,
            price=price,
            category=category,
            description=description,
            quantity=quantity,
            is_active=is_available,
            image=image
        )
        created_product.save()  

        return redirect('/dashboard')
    
    return render(request, 'seller/add_product.html')

def delete_product(request,product_id):
    product=Product.objects.get(id=product_id)
    print(product)
    product.delete()
    
    return redirect("/dashbord")

def update_product(request,product_id):
    data={}
    product=Product.objects.filter(id=product_id)
    print(product)#queryset
    print(product[0])#only one object
    data['product']=product[0]
    return render(request,'seller/update_product.html',context=data)

def view_products(request):
    data={}
    products=Product.objects.all()
    data['products']=products
    return render(request,'seller/products.html', context=data)