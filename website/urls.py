from django.urls import path
from . import views
app_name = 'website'
urlpatterns =[
    path('' ,views.home,name = 'home'),
    path('contact-us' ,views.contact,name = 'contact-us'),
    path('about-us' ,views.about,name = 'about-us'),
    path('tag/<int:tag_name>/',views.tag,name = 'tag'),
    path('blog/<int:id>/',views.post,name = 'post'),
]