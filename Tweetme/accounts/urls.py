from django.urls import path,re_path
from .views import UserDetailView,UserFollowView
urlpatterns = [
    
    path('<str:username>/',UserDetailView.as_view(),name='detail'),   
    
    path('<str:username>/follow',UserFollowView.as_view(),name='follow'), 
    # path('create/',TweetCreateView.as_view(),name = 'create'),
    # re_path(r'^(?P<pk>\d+)/edit',TweetUpdateView.as_view(),name='update'),   
    # re_path(r'^(?P<pk>\d+)/delete',TweetDeleteView.as_view(),name='delete'),
]
app_name = 'accounts'