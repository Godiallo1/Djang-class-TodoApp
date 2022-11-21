from django.urls import path
from .import views


urlpatterns = [
    path('', views.todo, name= 'todo'),
    path('update/<int:pk>', views.updateitem, name='updateitem'),
    path('delete/<int:pk>', views.deleteitem, name='deleteitem'),
]