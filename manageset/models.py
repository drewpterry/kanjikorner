from __future__ import division
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import random
from datetime import datetime, timedelta, time


# Create your models here.

class Kanji(models.Model):
    kanji_name = models.CharField(max_length = 50)
    kanji_meaning = models.CharField(max_length = 200)
    readings = models.CharField(max_length = 200, null = True)
    on_kun_readings = models.CharField(max_length = 200, null = True)
    strokes = models.IntegerField(null = True)
    grade = models.IntegerField(null = True)
    newspaper_frequency = models.IntegerField(null = True)
    jlpt_level = models.IntegerField(null = True)
    jinmeiyo = models.BooleanField(default = False)
    date_added = models.DateTimeField(auto_now_add = True, null = True)
    
    def __unicode__(self):
        return self.kanji_name


class Words(models.Model):
    real_word = models.CharField(max_length = 300)
    meaning = models.CharField(max_length = 500)
    hiragana = models.CharField(max_length = 301)
    frequency = models.IntegerField(db_index = True)
    frequency_two = models.IntegerField(db_index = True, null = True)
    combined_frequency = models.IntegerField(db_index = True, null = True)
    frequency_thousand = models.IntegerField(db_index = True, null = True)
    part_of_speech = models.CharField(max_length = 200, null = True)
    kanji = models.ManyToManyField(Kanji, blank = True)
    duplicate_word = models.BooleanField(default = False)
    published = models.BooleanField(default = True)
    
    def combine_frequencies(self):
        
        
        frequency_bonus = 0
        frequency_again = 0
        if self.frequency_two == None:
            frequency_again = 0
        else:
            frequency_again = self.frequency_two

        # print self.frequency

        if self.frequency > 0:
           
            frequency_bonus = self.frequency - 49
            frequency_bonus = frequency_bonus * (-1)
            frequency_bonus = frequency_bonus * 5 + 230

        self.combined_frequency = frequency_bonus + frequency_again
        return self.combined_frequency
            
    
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


from registration.signals import user_registered
def createUserProfile(sender, user, request, **kwargs):
    UserProfile.objects.get_or_create(user=user)

user_registered.connect(createUserProfile)

class KnownKanji(models.Model):
    kanji = models.ManyToManyField(Kanji)
    date_added = models.DateTimeField(auto_now_add = True)
    selected_kanji = models.BooleanField(default = False)
    user_profile = models.ManyToManyField(UserProfile)
    
    #im not sure what this is for....
    number_of_chosen_words = models.IntegerField(null = True)
    
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
    times_answered_correct = models.IntegerField(default = 0)
    times_answered_wrong = models.IntegerField(default = 0)
    correct_percentage = models.FloatField(null = True)
    
    
    def update_tier_and_review_time(self, correct):
        options = {     0 : None,
                        1 : 3.5,
                        2 : 23,
                        3 : 70,
                        # 7.7 days (multiply by 2.4)
                        4 : 180,
                        5 : 432,
                        # 1.5 months
                        6 : 1036,
                        # 3.4 months
                        7 : 2488,
                        # 8 months
                        8 : 5820,
                        9 : None,
        }
        if correct == 1:
            self.times_answered_correct = self.times_answered_correct + 1
            if self.tier_level < 9: 
                self.tier_level = self.tier_level + 1
        elif self.tier_level != 1:
            self.times_answered_wrong = self.times_answered_wrong + 1 
            self.tier_level = self.tier_level - 1
        elif self.tier_level == 1:
            self.times_answered_wrong = self.times_answered_wrong + 1   
        
        total_times_answered = self.times_answered_correct + self.times_answered_wrong
        self.correct_percentage = self.times_answered_correct / total_times_answered
        new_hours = options[self.tier_level]
        random_multiplier = random.uniform(.95, 1.05)
        
        self.last_practiced = datetime.now()
        self.time_until_review = timedelta(hours = new_hours).total_seconds() * random_multiplier
                    
        return
        
    def times_practiced(self):
        total_times_practiced = self.times_answered_correct + self.times_answered_wrong
        return total_times_practiced
        
   
    
    def __unicode__(self):
        return self.words.real_word

            
