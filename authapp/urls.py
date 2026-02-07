from django.urls import path
from authapp import views
from django.contrib.auth import views as auth_views # inbuilt views

urlpatterns = [
    path('signup/',views.signup_view,name='signup'),
    path('',views.home_view,name='home'),
    path('about/',views.about_view,name='about'),
    path('login/',views.login_view,name='login'),
    path('recent/',views.recent_view,name='recent'),
    path('logout/',views.logout_view,name='logout'),


    # for password change
    path('change_password/', views.new_password, name='change_password'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]