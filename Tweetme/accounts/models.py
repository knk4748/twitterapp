from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.db.models.signals  import post_save


class UserProfileManager(models.Manager):
    use_for_related_fields = True

    def all(self):
        qs = self.get_queryset().all()
        print("debug333")
        if self.instance:
            print("debug222")
            qs=qs.exclude(user = self.instance)
    
        return qs    
    def toggle_follow(self,user,to_toggle_user):
        user_profile,created = UserProfile.objects.get_or_create(user=user)  # returns a tuple like (userObj,true)
        if to_toggle_user in user_profile.following.all():
            user_profile.following.remove(to_toggle_user)
            added = True
        else:
            user_profile.following.add(to_toggle_user)
            added = False
        return  added      

    def is_following(self,user,followed_by_user):
        user_profile,created = UserProfile.objects.get_or_create(user=user)  # returns a tuple like (userObj,true)
        if created:
            return False
        if followed_by_user in user_profile.following.all():
            return True    
        return False
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='account')
    following = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='followed_by')


    objects=UserProfileManager()


    def __str__(self):
        return (self.user.username + " " + str(self.following.all().count()))

    def get_following(self):
        users = self.following.all()
        return users.exclude(username = self.user.username)

    def get_follow_url(self):
        return reverse_lazy("accounts:follow", kwargs={"username":self.user.username} )

    def get_absolute_url(self):
        return reverse("accounts:detail", kwargs={"username":self.user.username})
    


def post_save_user_receiver(sender,instance,created,*args, **kwargs):
    print(instance)
    if created:
        new_profile = UserProfile.objects.get_or_create(user=instance) #new profile is a tuple
         


post_save.connect(post_save_user_receiver,sender = settings.AUTH_USER_MODEL)    