from django.urls import path
from User import views
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetConfirmForm, UserPasswordResetForm
urlpatterns = [
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='User/password-reset-form.html',form_class=UserPasswordResetForm),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='User/password-reset-done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="User/password-reset-confirm.html",form_class=UserPasswordResetConfirmForm),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="User/password-reset-complete.html"),name='password_reset_complete'),
]