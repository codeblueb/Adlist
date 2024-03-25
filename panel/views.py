from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from django.core.files.storage import FileSystemStorage
from news.models import Article

from ipware import get_client_ip
# import datetime
from subcategory.models import Sub_Category

def panel(request):
    
    ip, ip_routable = get_client_ip(request)
    
    if ip is None:
        ip = "0.0.0.0"
    else:
        if ip_routable:
            ipv = "Public"
        else:
            ipv = "Private"
    print(ip, ipv)
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'back/home.html', context)
    
class ArticleListView(ListView):
    
    model = Article
    news = Article.objects.all()
    context_object_name = 'articles'    
    template_name = "back/news/news_lists.html"

def news_add(request):
    
    # now = datetime.datetime.now()
    # year = now.year 
    # month = now.month
    # day = now.day
    
    # # this will add a 0 to single digit day and same for the month
    # if len(str(day)) == 1:
    #     day = "0" + str(day)
    # if len(str(month)) == 1:
    #     month = "0" + str(month)
        
    # print(str(year) + "/" + str(month) + "/" + str(day))
    
    categories = Sub_Category.objects.all()
    
    if request.method == "POST":
        newsarticlename = request.POST.get('newsarticlename')
        newsauthor = request.POST.get('newsauthor')
        newscategory = request.POST.get('newscategory')
        newsshorttitle = request.POST.get('newsshorttitle')
        newsbody = request.POST.get('newsbody')
        newsid = request.POST.get('newscategory')
        
        if newsauthor == "" or newsshorttitle == "" or newsbody == "" or newscategory == "":
            errors = {
                "error": "All Fields Required!",
            }
            return render(request, 'back/news/errors/add_error.html', errors)
        
        # Adding a check for if the file is an image or a non image file 
        # File requirements
        try: 
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
                
            if str(myfile.content_type).startswith("image"):
                
                # we can only accept images less than 5MB
                if myfile.size < 5000000:
                    
                    article_name = Sub_Category.objects.get(pk=newsid).name
                    data = Article(article=newsarticlename, authur=newsauthor, title=newsshorttitle,
                                body=newsbody, category_name=article_name, image=filename, image_url=url, 
                                category_id=newsid, views=0)
                    data.save()
                    return redirect('article_lists') # you can redirect to this page if preferred 
                else:
                    try:
                        fs = FileSystemStorage()
                        fs.delete(filename)
                    except OSError as e:
                        if e.errno != errno.ENOENT:
                            raise
                    errors = { "error": "Your File Exceeds 5MB limit!" }
                    return render(request, 'back/news/errors/add_error.html', errors)
            else:
                try:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                except OSError as e:
                    if e.errno != errno.ENOENT:
                        raise
                errors = { "error": "Your File Not Supported!" }
                return render(request, 'back/news/errors/add_error.html', errors)
        except:
            errors = { "error": "Please Input Your Image!" }
            return render(request, 'back/news/errors/add_error.html', errors)
    return render(request, "back/news/news_add.html", {'categories':categories})

def news_delete(request, pk):
    
    b = Article.objects.get(pk=pk)
    fs = FileSystemStorage(b.image_url)
    
    if fs.url(b.image_url):
        import os
        from pathlib import Path
        get_base = Path(__file__).resolve().parent.parent
        file_for_deletion = str(get_base) + str(b.image_url)
        
        try:
            # fs.delete(b.image_url) # this is not working here, check later
            os.remove(file_for_deletion)
        except OSError as e:
            if e.errno != errno.ENOENT:
                raise
    b.delete()
    return redirect('article_lists') 

def news_edit(request, pk):
    
    if len(Article.objects.filter(pk=pk)) == 0:
        error = "Article not Found!"
        return render(request, 'back/news/errors/add_error.html', {'error':error})
    
    news = Article.objects.get(pk=pk)
    categories = Sub_Category.objects.all()
    
    if request.method == "POST":
        newsarticlename = request.POST.get('newsarticlename')
        newsauthor = request.POST.get('newsauthor')
        newscategory = request.POST.get('newscategory')
        newsshorttitle = request.POST.get('newsshorttitle')
        newsbody = request.POST.get('newsbody')
        newsid = request.POST.get('newscategory')
        
        if newsauthor == "" or newsshorttitle == "" or newsbody == "" or newscategory == "":
            errors = {
                "error": "All Fields Required!",
            }
            return render(request, 'back/news/errors/add_error.html', errors)
        
        # Adding a check for if the file is an image or a non image file 
        # File requirements
        try: 
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
                
            if str(myfile.content_type).startswith("image"):
                
                # we can only accept imagers less than 5MB
                if myfile.size < 5000000:                    
                    category_name = Sub_Category.objects.get(pk=newsid).name
                    # try:
                    #     fs = FileSystemStorage()
                    #     fs.delete(filename)
                    # except OSError as e:
                    #     if e.errno != errno.ENOENT:
                    #         raise
                    b = Article.objects.get(pk=pk)
                    b.article = newsarticlename
                    b.title = newsshorttitle
                    b.body = newsbody
                    b.image = filename
                    b.image_url = url
                    b.category_name = category_name
                    b.category_id = newsid
                    b.save()
                    return redirect('article_lists') 
                else:
                    try:
                        fs = FileSystemStorage()
                        fs.delete(filename)
                    except OSError as e:
                        if e.errno != errno.ENOENT:
                            raise
                    errors = { "error": "Your File Exceeds 5MB limit!" }
                    return render(request, 'back/news/errors/add_error.html', errors)
            else:
                try:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                except OSError as e:
                    if e.errno != errno.ENOENT:
                        raise
                errors = { "error": "Your File Not Supported!" }
                return render(request, 'back/news/errors/add_error.html', errors)
        except:
            category_name = Sub_Category.objects.get(pk=newsid).name
        
            b = Article.objects.get(pk=pk)
            b.article = newsarticlename
            b.title = newsshorttitle
            b.body = newsbody
            b.category_name = category_name
            b.category_id = newsid
            b.save()
            return redirect('article_lists') 
    return render(request, 'back/news/news_edit.html', {'pk':pk, 'categories':categories, 'news': news})