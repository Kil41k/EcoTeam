from django.urls import path
from .views import register, user_login, profile, complete, logoutview, userChangeView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/<int:user_id>/', profile, name='profile'),
    path('logout/', logoutview, name='logout'),
    path('changeprofdata/', userChangeView, name='redak'),
    path('complete/<int:aproj_id>/', complete, name='completeproj')
]
