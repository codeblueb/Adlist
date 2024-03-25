from django.shortcuts import render, get_object_or_404, redirect

from .models import Category

def category_list(request):
    
    cat = Category.objects.all()
    return render(request, 'back/category/category_list.html', { "cat": cat})

def category_add(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        if name == "":
            error = "Must Inter A Category"
            return render(request, 'back/news/errors/add_error.html', {"error": error})
        if len(Category.objects.filter(name=name)) != 0:
            error = "This Category already exists."
            return render(request, 'back/news/errors/add_error.html', {"error": error})
        b = Category(name=name)
        b.save()
        return redirect('category_list')
    return render(request, 'back/category/category_add.html')