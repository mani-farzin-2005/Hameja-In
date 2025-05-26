from django.urls import path
from . import views
app_name = 'blog'
urlpatterns =[
    path('' ,views.test,name = 'home'),
    #path('blog-name' ,views.test,name = 'single'),
    #path('author' ,views.test,name = 'author'),
    #path('tag' ,views.test,name = 'tags'),
]