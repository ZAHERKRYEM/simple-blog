
from django.urls import path
from . import views

app_name='app'
urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name= 'about'),
    path('contact/', views.contact,name= 'contact'),
    path('post/<int:id>', views.post,name= 'post'),
]
