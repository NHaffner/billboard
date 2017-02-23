from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$',views.post_new, name="post_new"),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^app/post/$', views.app_post, name='app_post'),
]