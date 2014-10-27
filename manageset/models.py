from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Kanji(models.Model):
    kanji_name = models.CharField(max_length = 50)
    kanji_meaning = models.CharField(max_length = 200)
    readings = models.CharField(max_length = 200)
    strokes = models.IntegerField()
    grade = models.IntegerField()
    
    def __unicode__(self):
        return self.kanji_name


class Words(models.Model):
    real_word = models.CharField(max_length = 200)
    meaning = models.CharField(max_length = 500)
    hiragana = models.CharField(max_length = 200)
    frequency = models.IntegerField()
    kanji = models.ManyToManyField(Kanji, blank = True)
    
    def __unicode__(self):
        return self.real_word
    

class Sets(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("pub_date")
    words = models.ManyToManyField(Words, blank = True)
    kanji = models.ManyToManyField(Kanji, blank = True)
    # userprofile = models.ForeignKey(UserProfile)
    
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_sets = models.ManyToManyField(Sets, blank = True)
    known_kanji = models.ManyToManyField(Kanji, blank = True)
    known_words = models.ManyToManyField(Words, blank = True)
    
    
    def __unicode__(self):
        return unicode(self.user)


            
