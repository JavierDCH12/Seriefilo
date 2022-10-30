from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name="index"),
    path('', views.index, name="inicio"),
    path('series/', views.list, name="list"),
    path('category/<str:genre>', views.category, name="category"),
    path('platform/<str:wheretosee>', views.platform, name="platform"),
    path('serie/<str:title>', views.serie, name="serie"),
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout")







    


]