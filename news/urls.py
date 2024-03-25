from django.urls import path
# from news.views import ArticleDetailsView
# from . import views
from .views import ArticleDetailView, ArticleListView

urlpatterns = [
    # path('', ArticleDetailsView.as_view(), name="article-details"),
    path('<slug:slug>/', ArticleDetailView.as_view(), name="article_details"),
    path('list/', ArticleListView.as_view(), name="news_list"),
]