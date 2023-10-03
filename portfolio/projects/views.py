from django.shortcuts import render

from .models import Category, Item

def projects(request):
    items = Item.objects.all()
    categories = Category.objects.all()

    return render(request, 'projects/projects.html', {
        'categories': categories,
        'items': items,
    })
