from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Stock
from .forms import StockForm


def root (request):
    return HttpResponse('Hello Django and Docker')

def hello_world(request):
    return render(request, 'testapp/hello.html')

def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'testapp/stock_list.html', {'stocks': stocks})

def stock_add(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = StockForm()
    return render(request, 'testapp/stock_form.html', {'form': form, 'action': 'add'})

def stock_edit(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = StockForm(instance=stock)
    return render(request, 'testapp/stock_form.html', {'form': form, 'action': 'edit'})