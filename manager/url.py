from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^words/$', views.words.as_view(), name='words'),
    re_path(r'^categories/$', views.categories.as_view(), name='categories'),
    re_path(r'^categories/(?P<pk>\d+)$', views.categories_detail.as_view(), name='categories_detail')

]
