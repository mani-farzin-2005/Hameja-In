from django.urls import path
from . import views
app_name = 'tour'
urlpatterns =[
    path('' ,views.home,name = 'home'),
    path('tag/<str:name>' , views.tag , name ='tag'),
    path('tour/<int:id>' , views.single , name ='tour'),
    path('alltour' , views.all_tour , name ='all-tour'),
    path('package/<int:id>' , views.Package , name ='package'),
]