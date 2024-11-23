"""
URL Configuration for the Account Application

This module defines URL patterns for the account-related views in the application.
Each URL pattern is associated with a view that handles user registration, login,
logout, profile management, password reset, and follow/unfollow actions.

Routes:
    - 'register/': User Registration
    - 'login/': User Login
    - 'logout/': User Logout
    - 'profile/<int:pk>/': User Profile
    - 'reset/': Password Reset
    - 'reset/done/': Password Reset Done
    - 'confirm/<uidb64>/<token>/': Password Reset Confirmation
    - 'confirm/complete/': Password Reset Complete
    - 'follow/<int:user_id>/': Follow a User
    - 'unfollow/<int:user>/': Unfollow a User
    - 'edit_user/': Edit User Information
"""

from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='user_profile'),
    path('reset/', views.UserPasswordResetView.as_view(), name='user_password_reset'),
    path('reset/done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('confirm/complete/', views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('follow/<int:user_id>/', views.UserFollowView.as_view(), name='user_follow'),
    path('unfollow/<int:user>/', views.UserUnfollowView.as_view(), name='user_unfollow'),
    path("edit_user/", views.EditUserView.as_view(), name="edit_user")
]
