from django.shortcuts import render, get_object_or_404, redirect

from .models import Category, Item

def projects(request):
    items = Item.objects.all()
    categories = Category.objects.all()

    return render(request, 'projects/projects.html', {
        'categories': categories,
        'items': items,
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'projects/detail.html', {
        'item': item,
    })