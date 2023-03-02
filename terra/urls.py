from django.urls import path

from . import views

app_name = 'terra'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('info/<int:pk>/', views.InfoView.as_view(), name='info'),
    path('login_register/', views.LoginRegisterView.as_view(), name='login_register'),
    # path('buy/<int:terrarium_id>/', views.buy, name='buy'),
    path('logout/', views.logout_view, name='logout'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add_to_cart/',views.add_to_cart, name='add_to_cart'),
    # path('',views.index, name='index'),
]
