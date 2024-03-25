# from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from .models import Article

# class ArticleDetailsView(DetailView):
    
#     template_name = "pages/article_details.html"
    
#     # self relates to instance
#     def get_context_data(self, *args, **kwargs):
#         context = super(ArticleDetailsView, self).get_context_data(*args, **kwargs)
#         return context
    
#     # this is handling all the querysets
#     def get_queryset(self, *args, **kwargs):
#         request = self.request
#         pk = self.kwargs.get('pk')
#         instance = Article.objects.get_by_id(pk)
#         if instance is None:
#             raise Http404("Article does not exists")
#         return instance 
    
# class ArticleDetailSlugView(DetailView):
    
#     queryset = Article.objects.all()
#     template_name = "pages/article_details.html"
    
#     def get_object(self, *args, **kwargs):
#         request = self.request
#         slug = self.kwargs.get('slug')
        
#         try:
#             instance = Article.objects.get(slug=slug, active=True)
#         except Article.DoesNotExist:
#             raise Http404("404 - Not Found")
#         except Article.MultipleObjectsReturned:
#             qs = Article.objects.filter(slug=slug, active=True)
#             instance = qs.first()
#         except:
#             raise Http404("404 error")
#         return instance

class ArticleDetailView(DetailView):
    
    context = "News | Details"
    model = Article
    template_name = "front/news/article_details.html"

class ArticleListView(ListView):
    
    context = "News | Lists"
    model = Article
    template_name = "back/news/news_lists.html"


    