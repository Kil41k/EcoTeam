from django.urls import path
from .views import indexview, create, category, about, joinproj, completeproj

urlpatterns = [
    path('', indexview, name='index'),
    path('create/', create, name='create'),
    path('category/<int:cat_id>/', category, name='category'),
    path('about/<int:proj_id>/', about, name='about'),
    path('joinproj/<int:proj_id>/', joinproj, name='joinproj'),
    path('completeproj/<int:proj_id>/', completeproj, name='completeproj'),

]