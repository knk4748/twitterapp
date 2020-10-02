from rest_framework import generics
from tweets.models import Tweet
from .serializers import TweetModelSerializer
from django.db.models import Q
from rest_framework import permissions
from .pagination import StandardResultsPagination


class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

  
    # def get_queryset(self,*args,**kwargs):
    def get_queryset(self,*args,**kwargs):
        im_following = self.request.user.account.get_following()

        print(im_following )
        print("OK  OK  OK  OK")
        qs1 = Tweet.objects.filter(user__in=im_following)
        qs_me = Tweet.objects.filter(user=self.request.user)
        qs = (qs1 | qs_me).distinct().order_by('-timestamp')
        query = self.request.GET.get('q',None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                )
        return qs    