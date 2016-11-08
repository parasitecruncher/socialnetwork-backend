from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField
from tastypie.utils.timezone import now
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from rest_framework.authtoken.models import Token
import uuid

class Profile(models.Model):
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        # formatter = HtmlFormatter(nick_name=self.nick_name,display_image=self.display_image,  full=True)
        # lexer=get_lexer_by_name(None)
        #self.highlighted = highlight(self.user ,lexer,formatter)
        super(Profile, self).save(*args, **kwargs)
    owner = models.OneToOneField('auth.User', related_name='Profile')
    #highlighted = models.TextField()
    user=models.OneToOneField(User)
    nick_name=models.CharField(max_length=10)
    about_me=models.CharField(max_length=300,blank=True)
    friends=models.ManyToManyField('self',blank=True)
    display_image=models.ImageField(blank=True)
    def __str__(self):
        return self.nick_name
    # def __unicode__(self):
    #     return unicode(self.nick_name)
class UserImages(models.Model):
    owner = models.ForeignKey('auth.User')
    user=models.ForeignKey(Profile)
    # highlighted = models.TextField(default=None,blank=True,null=True)
    image=models.ImageField()
    pub_date=models.DateTimeField(default=now)

class Like(models.Model):
    #nick_name=models.CharField(max_length=10)
    post = models.ForeignKey(UserImages)
    user = models.ForeignKey(Profile, related_name='liker')
    date_created = models.DateTimeField(auto_now_add=True)