from app import views
from django.urls import path, include
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
]