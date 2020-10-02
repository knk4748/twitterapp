from django.shortcuts import render
from .models import Tweet
from django.views.generic import DeleteView,DetailView,UpdateView,ListView,CreateView
from django.forms.utils import ErrorList
from .forms import TweetModelForm
from django.db.models import Q
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# def tweet_detail_view(request):
#     return render(request,"tweets/detail_view.html",{})




# def tweet_list_view(request):
#     return render(request,"tweets/detail_list .html",{})


class TweetListView(ListView):
    model = Tweet
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy('tweets:create')
        return context

    def get_queryset(self,*args,**kwargs):
        im_following = self.request.user.account.get_following()
        print(im_following )
        print("OK  OK  OK  OK")
        qs = Tweet.objects.filter(user__in=im_following)
        query = self.request.GET.get('q',None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                )
        return qs    


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get("pk") 
        return Tweet.objects.get(id=pk )    



class TweetCreateView( LoginRequiredMixin,CreateView):    
    form_class = TweetModelForm
    # model = Tweet
    template_name = 'tweets/create_view.html'
    # success_url = 'tweets/create_view.html'
    login_url = "/admin/"
    
    # fields = ['user','content']     
    def form_valid(self,form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super(TweetCreateView,self).form_valid(form)
        # else:
        #     form._errors[forms.forms.NON_FIELD_ERRORS]= ErrorList(["User must be logged in"])
        #     return self.form_invalid(form)
class TweetUpdateView(UpdateView):
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = '/tweet/'
    model = Tweet 

class  TweetDeleteView(LoginRequiredMixin,DeleteView):
    model = Tweet
    success_url = reverse_lazy("tweets:list")
    template_name='tweets/delete_confirm.html'
    # success_url = reverse_lazy("home") 