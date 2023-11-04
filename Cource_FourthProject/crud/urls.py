from django.urls import path
from crud import views

urlpatterns = [
    path('', views.PersonListView.as_view(), name='all'),
    path('create/', views.PersonCreateView.as_view(), name='person_create'),
    path('edit/<int:pk>/', views.PersonUpdateView.as_view(), name='person_update'),
    path('delete/<int:pk>/', views.PersonDeleteView.as_view(), name='person_delete'),
]
