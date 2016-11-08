from django.conf.urls import url,include
from main import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers




urlpatterns = [
    url(r'^im/$', views.ImagesViewSet.as_view({'get': 'retrieve'})),
    url(r'^profiles/$', views.Profile_List.as_view()),
    url(r'^profiles/(?P<pk>[0-9]+)/$', views.Profile_Detail.as_view()),
    url(r'^users/$', views.User_List.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.User_Detail.as_view()),
    url(r'^clog/',views.Login.as_view()),
    url(r'^friends/',views.MyFriends.as_view()),
    url(r'^feed/$',views.Feed.as_view()),
    url(r'^feed/(?P<pk>[0-9]+)/$',views.UserFeed.as_view()),
    url(r'^images/(?P<pk>[0-9]+)/$',views.ImagesDetail.as_view()),
    url(r'^images/$',views.ImagesAll.as_view()),
    url(r'^search/$',views.Search.as_view()),
    url(r'^likes/$',views.Like_List.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)