from django.db import models

class Tweet(models.Model):
    user_id  = models.CharField(blank=True, max_length=200,null=True)
    user_name = models.CharField(blank=True, max_length=200,null=True)
    user_screenname = models.CharField(blank=True, max_length=200,null=True)
    user_location = models.CharField(blank=True, max_length=500,null=True)
    user_followers = models.IntegerField(default=0)
    user_friends = models.IntegerField(default=0)
    t_id = models.IntegerField(default=0)
    t_rtcount = models.IntegerField(default=0)
    t_favcount = models.IntegerField(default=0)
    t_create = models.DateTimeField(blank=True, null=True)
    t_text = models.TextField(blank=True)
    lang = models.CharField(blank=True, max_length=200,null=True)

    def __str__(self):
        return (self.user_screenname + str(self.t_id)) #returns uses screen name with tweet id
