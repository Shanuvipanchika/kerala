from django.urls import path
from.import views
urlpatterns = [
    path("xyz",views.efg),
    path("login",views.abcd,name='log-in'),
    path("home",views.first,name='ho-me'),
    path("new",views.new,name='new'),
    path("welcome",views.index,name='welcome'),
]