from django.conf.urls import url


from django.urls import path
from .views import polls_list, polls_detail, article_list



urlpatterns = [
    path("polls/", polls_list, name="polls_list"),
    path("polls/<int:pk>/", polls_detail, name="polls_detail"),
    path('article/',article_list, name="article_list"),
]
