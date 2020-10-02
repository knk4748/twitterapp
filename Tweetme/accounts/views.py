from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.views.generic import DetailView,View

from .models import UserProfile
# Create your views here.
User = get_user_model()

class UserDetailView(DetailView): 
    model = User
    template_name = 'accounts/user_detail.html'


    def get_object(self,*args, **kwargs):
        return get_object_or_404(User,username__iexact=self.kwargs.get("username"))
    
    def get_context_data(self,*args, **kwargs):
        context = super(UserDetailView,self).get_context_data(*args, **kwargs)
        context["following"] = UserProfile.objects.is_following(self.request.user,self.get_object())
        return context


class UserFollowView(View):
    def get(self,request,username,*args, **kwargs):
        toggle_user = get_object_or_404(User,username__iexact = username)
        if request.user.is_authenticated:
            isfollowing = UserProfile.objects.toggle_follow(request.user,toggle_user)

        return redirect("accounts:detail",username=username) 