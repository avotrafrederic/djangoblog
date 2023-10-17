from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,  name="test"),
    path("article",views.articles, name="article"),
    path("article/show/<int:id>",views.showArticle, name="article.show")
]
