from rest_framework import serializers
from accounts.api.serializers import UserDisplaySerializer
from django.utils.timesince import timesince
from tweets.models import Tweet


class TweetModelSerializer(serializers.ModelSerializer ):
    user = UserDisplaySerializer(read_only=True)
    date_display  = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()


    class Meta:
        model = Tweet
        fields = [
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince'
        ]
    def get_date_display(self,obj):
        return obj.timestamp.strftime("%b %d %I :%M %p ")

    def get_timesince(self,obj):
        return timesince(obj.timestamp) + " ago" 
