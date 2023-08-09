from django.urls import path
from . import views
app_name="gestion"
urlpatterns = [
    path('',views.index),
    
    path('detail/<int:pk>',views.show, name="show"),
]