from django.conf.urls import urls
from . import views


app_name = 'albums'
urlpatterns=[
    #/music/
    url(r'^$',views.index, name='index')
    #music/albumname
    #url()
]
