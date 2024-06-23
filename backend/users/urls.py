from django.urls import path
from .views import *

urlpatterns = [
    path('signup', signup, name="Signup"),
    path('login', login, name="Login"),
    path('test', test_token, name="test"),

]