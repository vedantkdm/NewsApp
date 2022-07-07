from django.urls import path
from . import  views
from .views import CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', views.home, name='home'),
    path('blog/', views.frontpage, name='blog'),
    path('<slug:slug>/',views.post_detail, name='post_detail'),
]
