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
    times_practiced = models.IntegerField()
    # userprofile = models.ForeignKey(UserProfile)
    
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_sets = models.ManyToManyField(Sets, blank = True)
    # known_kanji = models.ManyToManyField(Kanji, blank = True)
    # known_words = models.ManyToManyField(Words, blank = True)
    
    
    def __unicode__(self):
        return unicode(self.user)


class KnownKanji(models.Model):
    kanji = models.ManyToManyField(Kanji)
    date_added = models.DateTimeField(auto_now = True)
    selected_kanji = models.BooleanField(default = False)
    user_profile = models.ManyToManyField(UserProfile)
    
    def __unicode__(self):
        return unicode(self.kanji)

    
class KnownWords(models.Model):
    words = models.ForeignKey(Words)
    user_profile = models.ForeignKey(UserProfile)
    date_added = models.DateTimeField(auto_now = True)
    tier_level = models.IntegerField()
    last_practiced = models.DateTimeField(blank = True)
    # remaining_time_review = models.FloatField(null = True)
    time_until_review = models.FloatField(null = True)
    
    def __unicode__(self):
        return self.words.real_word

            
