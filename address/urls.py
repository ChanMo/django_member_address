from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.AddressListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.AddressDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.AddressUpdateView.as_view(), name='update'),
    url(r'^create/$', views.AddressCreateView.as_view(), name='create'),
]
