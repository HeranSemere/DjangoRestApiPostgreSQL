from django.urls import re_path 
from mindplex import views 
 
urlpatterns = [ 
    re_path(r'^api/mindplex/articles$', views.articles_list),
    re_path(r'^api/mindplex/articles/(?P<pk>[0-9]+)$', views.articles_detail),
    re_path(r'^api/mindplex/interactions$', views.interactions_list),
    re_path(r'^api/mindplex/interactions/(?P<pk>[0-9]+)$', views.interactions_detail),
    re_path(r'^api/mindplex/recommendationconfiguration$', views.recommendationconfiguration_list),
    re_path(r'^api/mindplex/recommendationconfiguration/(?P<pk>[0-9]+)$', views.recommendationconfiguration_detail),
    re_path(r'^api/mindplex/recommendation/(?P<pk>[0-9]+)$', views.recommendation)
]