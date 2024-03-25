from django.urls import path

from .views import ArticleListView
from . import views

from category.views import category_list, category_add
from subcategory.views import subcategory_list, subcategory_add

urlpatterns = [
    path('', views.panel, name="panel"),
    path('news/list/', ArticleListView.as_view(), name="article_lists"),
    path('news/add/', views.news_add, name="article_add"),
    # path('news/del/(?P<pk>\d+)', views.news_delete, name="article_delete"),
    path('news/del/<int:pk>', views.news_delete, name="article_delete"),
    path('news/edit/<int:pk>', views.news_edit, name="article_edit"),
    path("category/list/", category_list, name="category_list"),
    path("category/add/", category_add, name="category_add"),
    path("subcategory/list/", subcategory_list, name="subcategory_list"),
    path("subcategory/add/", subcategory_add, name="subcategory_add"),
]
