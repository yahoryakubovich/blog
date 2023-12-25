from django.urls import path
from .views import ArticleListView, ArticleDetailView,  ArticleCreateView, CommentCreateView

urlpatterns = [
    path('article_list/', ArticleListView.as_view(), name='article-list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/create/', ArticleCreateView.as_view(), name="article-create"),
    path('article/<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
]
