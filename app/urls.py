from app import views
from django.urls import path, include
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
]