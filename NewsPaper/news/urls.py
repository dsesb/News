from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, PostDetail, SearchList, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>/', PostDetail.as_view(), name='post'),
   path('search/', SearchList.as_view()),
   path('create/', PostCreateView.as_view(), name='post_create'),
   path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
   path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]