from django.urls import path

from API import views

urlpatterns = [
    # path('books/', views.BookListView.as_view(), name='list'),
    path('books/', views.BookList)
]