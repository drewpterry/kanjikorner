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
    real_word = models.CharField(max_length = 300)
    meaning = models.CharField(max_length = 500)
    hiragana = models.CharField(max_length = 301)
    frequency = models.IntegerField(db_index = True)
    frequency_two = models.IntegerField(db_index = True, null = True)
    part_of_speech = models.CharField(max_length = 200, null = True)
    kanji = models.ManyToManyField(Kanji, blank = True)
    duplicate_word = models.BooleanField(default = False)
    published = models.BooleanField(default = True)
    
    def __unicode__(self):
        return self.real_word

class WordMeanings(models.Model):
    word = models.ForeignKey(Words)
    meaning = models.CharField(max_length = 500)
    
    def __unicode__(self):
        return self.meaning
    

class Sets(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("pub_date", auto_now_add = True)
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
    date_added = models.DateTimeField(auto_now_add = True)
    selected_kanji = models.BooleanField(default = False)
    user_profile = models.ManyToManyField(UserProfile)
    
    def __unicode__(self):
        return unicode(self.kanji)
        
    def display_kanji(self):
        return unicode(self.kanji)   

    
class KnownWords(models.Model):
    words = models.ForeignKey(Words)
    user_profile = models.ForeignKey(UserProfile)
    #last_checked -- need to add real date_added field and rename this one
    date_added = models.DateTimeField(auto_now_add = True)
    tier_level = models.IntegerField()
    last_practiced = models.DateTimeField(blank = True)
    # remaining_time_review = models.FloatField(null = True)
    time_until_review = models.FloatField(null = True)
    
    def __unicode__(self):
        return self.words.real_word

            
