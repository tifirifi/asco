from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tickets/$', views.ticket_list, name='ticket_list'),
    url(r'^tickets/(?P<pk>\d+)/$', views.ticket_detail, name='ticket_detail'),
    #url(r'^tickets/create/$', views.ticket_create, name='ticket_create'),
    #url(r'^tickets/(?P<pk>\d+)/delete/$', views.ticket_delete, name='ticket_delete'),
    #url(r'^tickets/(?P<pk>\d+)/edit/$', views.ticket_update, name='update'),
]