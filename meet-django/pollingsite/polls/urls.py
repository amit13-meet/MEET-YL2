from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	url(r'^homie/$', views.homie, name = "homie")
)
