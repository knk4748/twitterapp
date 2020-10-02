from .views import TweetDetailView,TweetDeleteView,TweetUpdateView,TweetListView,TweetCreateView
from django.urls import path,re_path
urlpatterns = [
    path('',TweetListView.as_view(),name='list'),
    re_path(r'^(?P<pk>\d+)/$',TweetDetailView.as_view(),name='detail'),   
    path('create/',TweetCreateView.as_view(),name = 'create'),
    re_path(r'^(?P<pk>\d+)/edit',TweetUpdateView.as_view(),name='update'),   
    re_path(r'^(?P<pk>\d+)/delete',TweetDeleteView.as_view(),name='delete'),
]
app_name = 'tweets'