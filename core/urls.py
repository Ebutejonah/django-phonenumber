from django.urls import path
from .views import register, profile, login,checkout,success


app_name = 'core'

urlpatterns = [
    path('', register, name="register"),
    path('login/',login, name='login'),
    path('profile/', profile, name="profile"),
    path('checkout/', checkout, name="checkout"),
    path('success/', success, name="success"),
]