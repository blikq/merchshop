from django.urls import path
from .views import *

urlpatterns = [
    path('signup', signup, name="Signup"),
    path('login', login, name="Login"),
    # path('test', test_token, name="test"),
    # path('verify_user/', verify_user, name="verify_user"),
    path('verify_email', confirm_email, name="confirm_email"),

]