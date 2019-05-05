from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.MyCreateView.as_view()),
]
