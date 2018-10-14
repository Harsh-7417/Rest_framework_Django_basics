from django.shortcuts import render,redirect
from .forum import productForm
from product.models import productModel


#from django.shortcuts import render,redirect







def get_list(request):
    products=productModel.objects.all()
    #print(products)
    return render(request,'prodcuts.html',{'products':products})

def create_new(request):
    form=productForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('get_list')
    return render(request,'Productform.html',{'form':form})

def update(request,id):
    product=productModel.objects.get(id=id)
    form=productForm(request.POST or None,instance=product)
    if form.is_valid():
        form.save()
        return redirect('get_list')
    return render(request,'Productform.html',{'form':form,'product':product})

def delete(request,id):
    product=productModel.objects.get(id=id)
    if request.method=='POST':
        product.delete()
        return redirect('get_list')
    return render(request,'product_del.html',{'product':product})


