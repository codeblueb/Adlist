from django.shortcuts import render, get_object_or_404, redirect

from .models import Sub_Category
from category.models import Category

def subcategory_list(request):
    
    subcat = Sub_Category.objects.all()
    return render(request, 'back/category/subcategory_list.html', { "subcat": subcat})

def subcategory_add(request):
    
    cat = Category.objects.all() 
    
    if request.method == 'POST':
        name = request.POST.get('name')
        catid = request.POST.get('subcategory')
        if name == "":
            error = "Must Inter A Category"
            return render(request, 'back/news/errors/add_error.html', {"error": error})
        if len(Sub_Category.objects.filter(name=name)) != 0:
            error = "This Category already exists."
            return render(request, 'back/news/errors/add_error.html', {"error": error})
        
        category_name = Category.objects.get(pk=catid).name
        
        b = Sub_Category(name=name, category_name=category_name, category_id=catid)
        b.save()
        return redirect('subcategory_list')
        
    return render(request, 'back/category/subcategory_add.html', {'cat':cat})