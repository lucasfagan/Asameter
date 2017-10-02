from django.conf.urls import url
from . import views


app_name = 'albums'
urlpatterns=[
    #/music/
    url(r'^$',views.index, name='index'),
    url(r'^sortfavorite/', views.sortfavorite, name='sortfavorite'),
    url(r'^sortalbum/', views.sortalbum, name='sortalbum'),
    url(r'^sortartist/', views.sortartist, name='sortartist'),
    url(r'^sortgenre/', views.sortgenre, name='sortgenre'),
    url(r'^(?P<selected_album>.+)/', views.detail, name='detail')



    #music/albumname
    #url()
]
