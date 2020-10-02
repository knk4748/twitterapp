from django.db import models
from django.contrib.auth.models import User
from .validators import validate_content
# Create your models here
from django.urls import reverse
 


class Tweet(models.Model):
    content = models.CharField(max_length=140,validators=[validate_content]) 
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.content)
    def get_absolute_url(self):
        return reverse("tweets:detail", kwargs={"pk": self.pk})
             
             

    class Meta:
        ordering = ['-timestamp']    
        
    # def clean(self,*args,**kwargs):
    #     content = self.content
    #     if content = self.content
    #     if content == "abc":
    #         raise Validationerror("Cannot be ABC")
    #     return super(Tweet,self).clean(*args,**kwargs)