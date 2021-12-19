from django.urls import path
from User import views
urlpatterns = [
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('changepassword',views.change_password,name="changepassword"),


]