from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Order, Gallery
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

# Create your views here.




@login_required
def index(request):
     orders = Order.objects.all()
     workers_count = User.objects.all().count()
     orders_count = Order.objects.all().count()
     product_count = Product.objects.all().count()
     if request.method=='POST':
          form = OrderForm(request.POST)
          if form.is_valid():
               instance = form.save(commit=False)
               instance.staff = request.user
               instance.save()
               return redirect('dashboard-index')
     else:
          form = OrderForm()
     context={
          'orders' : orders,
          'form' : form,
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/index.html', context)

@login_required
def graph(request):
     products = Product.objects.all().order_by('name')
     workers_count = User.objects.all().count()
     orders_count = Order.objects.all().count()
     product_count = Product.objects.all().count()
     context={
          'products' : products,
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/graph.html', context)


@login_required
def staff(request):
     workers = User.objects.all()
     workers_count = workers.count()
     orders_count = Order.objects.all().count()
     product_count = Product.objects.all().count()
     context={
          'workers' : workers,
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/staff.html', context)

@login_required
def staff_detail(request, pk):
     workers = User.objects.get(id=pk)
     context={
          'workers' : workers,
     }
     return render(request, 'dashboard/staff_detail.html', context)

@login_required
def staff_det(request):
    
     context={
          
     }
     return render(request, 'dashboard/staff_det.html', context)

@login_required
def product(request):
    
     items = Product.objects.all()  #orm
          
     #items = Product.objects.raw('SELECT * FROM dashboard_product')
     product_count = items.count()
     workers_count = User.objects.all().count()
     orders_count = Order.objects.all().count()

     context = {
          'items' : items,
          
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/product.html', context)

@login_required
def product_eee(request):
     items = Product.objects.all().filter(category='Electrical')      #orm     
     #items = Product.objects.raw('SELECT * FROM dashboard_product')
     product_count = items.count()
     workers_count = User.objects.all().count()
     orders_count = Order.objects.all().count()

     context = {
          'items' : items,
          
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/product_eee.html', context)

@login_required
def product_ece(request):
     
     items = Product.objects.all().filter(category='Electronics')      #orm
          
     #items = Product.objects.raw('SELECT * FROM dashboard_product')
     product_count = items.count()
     workers_count = User.objects.all().count()
     orders_count = Order.objects.all().count()

     context = {
          'items' : items,
          
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/product_ece.html', context)


@login_required
def product_mech(request):
    
     items = Product.objects.all().filter(category='Mechanical')      #orm
          
     #items = Product.objects.raw('SELECT * FROM dashboard_product')
     product_count = items.count()
     workers_count = User.objects.all().count()
     orders_count = Order.objects.all().count()

     context = {
          'items' : items,
          
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/product_mech.html', context)

@login_required
def product_civil(request):
    
     items = Product.objects.all().filter(category='Civil')      #orm
          
     #items = Product.objects.raw('SELECT * FROM dashboard_product')
     product_count = items.count()
     workers_count = User.objects.all().count()
     orders_count = Order.objects.all().count()

     context = {
          'items' : items,
          
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/product_civil.html', context)

@login_required
def product_cse(request):
    
     items = Product.objects.all().filter(category='Computer Science')      #orm
          
     #items = Product.objects.raw('SELECT * FROM dashboard_product')
     product_count = items.count()
     workers_count = User.objects.all().count()
     orders_count = Order.objects.all().count()

     context = {
          'items' : items,
          
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/product_cse.html', context)

@login_required
def product_add(request):
     if request.method == 'POST':
          form = ProductForm(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               product_name = form.cleaned_data.get('name')
               messages.success(request, f'{product_name} has been added')
               return redirect('dashboard-product-add')
     else:
          form = ProductForm()
     

     context = {
          'form' : form,

     }
     return render(request, 'dashboard/product_add.html', context)

@login_required
def product_delete(request, pk):
     item = Product.objects.get(id=pk)
     if request.method=='POST':
          item.delete()
          return redirect('dashboard-product')
     return render(request, 'dashboard/product_delete.html')   

@login_required
def product_update(request, pk):
     item = Product.objects.get(id=pk)
     if request.method=='POST':
          form = ProductForm(request.POST, request.FILES, instance=item)
          if form.is_valid():
               form.save()
               return redirect('dashboard-product')
     else:
          form = ProductForm(instance=item)
     context={
          'form' : form,

     }
     return render(request, 'dashboard/product_update.html', context)

@login_required
def order(request):
     orders = Order.objects.all()
     orders_count = orders.count()
     workers_count = User.objects.all().count()
     product_count = Product.objects.all().count()
     context={
          'orders' : orders,
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/order.html', context)




@login_required
def products_eee(request):
     items = Product.objects.all().filter(category='Electrical')      #orm     
     #items = Product.objects.raw('SELECT * FROM dashboard_product')
     product_count = items.count()
     workers_count = User.objects.all().count()
     orders_count = Order.objects.all().count()

     context = {
          'items' : items,
          
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/products-eee.html', context)

@login_required
def products_ece(request):
     
     items = Product.objects.all().filter(category='Electronics')      #orm
          
     #items = Product.objects.raw('SELECT * FROM dashboard_product')
     product_count = items.count()
     workers_count = User.objects.all().count()
     orders_count = Order.objects.all().count()

     context = {
          'items' : items,
          
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/products-ece.html', context)


@login_required
def products_mech(request):
    
     items = Product.objects.all().filter(category='Mechanical')      #orm
          
     #items = Product.objects.raw('SELECT * FROM dashboard_product')
     product_count = items.count()
     workers_count = User.objects.all().count()
     orders_count = Order.objects.all().count()

     context = {
          'items' : items,
          
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/products-mech.html', context)

@login_required
def products_civil(request):
    
     items = Product.objects.all().filter(category='Civil')      #orm
          
     #items = Product.objects.raw('SELECT * FROM dashboard_product')
     product_count = items.count()
     workers_count = User.objects.all().count()
     orders_count = Order.objects.all().count()

     context = {
          'items' : items,
          
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/products-civil.html', context)

@login_required
def products_cse(request):
    
     items = Product.objects.all().filter(category='Computer Science')      #orm
          
     #items = Product.objects.raw('SELECT * FROM dashboard_product')
     product_count = items.count()
     workers_count = User.objects.all().count()
     orders_count = Order.objects.all().count()

     context = {
          'items' : items,
          
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/products-cse.html', context)




@login_required
def product_search(request):
     if 'searched' in request.GET:
          searched = request.GET['searched']
          #items = Product.objects.filter(name__icontains=searched)
          multiple_searched = Q(Q(name__icontains=searched) | Q(category__icontains=searched) | Q(quantity__icontains=searched) | Q(Brand__icontains=searched))
          items = Product.objects.filter(multiple_searched)
     else:
          items = Product.objects.all()      #orm
          
     #items = Product.objects.raw('SELECT * FROM dashboard_product')
     product_count = items.count()
     workers_count = User.objects.all().count()
     orders_count = Order.objects.all().count()

     context = {
          'items' : items,
          
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/product_search.html', context)


@login_required
def products_search(request):
     if 'searched' in request.GET:
          searched = request.GET['searched']
          #items = Product.objects.filter(name__icontains=searched)
          multiple_searched = Q(Q(name__icontains=searched) | Q(category__icontains=searched) | Q(quantity__icontains=searched) | Q(Brand__icontains=searched))
          items = Product.objects.filter(multiple_searched)
     else:
          items = Product.objects.all()      #orm
          
     #items = Product.objects.raw('SELECT * FROM dashboard_product')
     product_count = items.count()
     workers_count = User.objects.all().count()
     orders_count = Order.objects.all().count()

     context = {
          'items' : items,
          
          'workers_count' : workers_count,
          'orders_count' : orders_count,
          'product_count' : product_count,
     }
     return render(request, 'dashboard/products-search.html', context)