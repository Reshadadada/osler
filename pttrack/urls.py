from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^intake/$', views.intake, name="intake"),
    url(r'^(?P<clindate>[0-9]{4}-[0-9]{2}-[0-9]{2})/$', views.clindate, name='clindate'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='patient')
]