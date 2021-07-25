from django.shortcuts import render
from app2.models import ProductModel
from django.shortcuts import redirect
# Create your views here.

def showMain(request):
    if request.method == 'POST':
        number = request.POST.get('p_no')
        name = request.POST.get('p_name')
        price = request.POST.get('p_price')
        image = request.FILES['p_image']
        ProductModel(number=number,name=name,price=price,image=image).save()
        return redirect('main')
    else:
        return render(request,'index.html',{'Product_info':ProductModel.objects.all()})


def showdeleteProduct(request,product_id):
    product_detail = ProductModel.objects.get(id=product_id)
    if request.method == 'POST':
        product_detail.delete()
        return redirect('main')
    else:
        return render(request,'del_product.html', {"prd":product_detail})
