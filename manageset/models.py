from __future__ import division
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import random
from datetime import datetime, timedelta, time
from django.utils import timezone

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
    twitter_frequency = models.FloatField(null = True)
    aozora_frequency = models.FloatField(null = True)
    wikipedia_frequency = models.FloatField(null = True)
    news_frequency = models.FloatField(null = True)
    date_added = models.DateTimeField(auto_now_add = True, null = True)
    master_order = models.IntegerField(null = True)

    def __unicode__(self):
        return self.kanji_name

class Words(models.Model):
    real_word = models.CharField(max_length = 300)
    meaning = models.CharField(max_length = 500)
    hiragana = models.CharField(max_length = 301)
    frequency = models.IntegerField(db_index = True, null = True, blank = True)
    frequency_two = models.IntegerField(db_index = True, null = True, blank = True)
    combined_frequency = models.IntegerField(db_index = True, null = True, blank = True)
    frequency_thousand = models.IntegerField(db_index = True, null = True, blank = True)
    part_of_speech = models.CharField(max_length = 200, null = True)
    kanji = models.ManyToManyField(Kanji, blank = True)
    duplicate_word = models.BooleanField(default = False)
    published = models.BooleanField(default = True)
    jlpt_level = models.IntegerField(db_index = True, null = True, blank = True)
    sentence_scrape = models.BooleanField(default = False)
    scrape_failed = models.BooleanField(default = False)
    master_order = models.IntegerField(null = True)
    reviewed = models.BooleanField(default = False)

    def combine_frequencies(self):
        frequency_bonus = 0
        frequency_again = 0
        if self.frequency_two == None:
            frequency_again = 0
        else:
            frequency_again = self.frequency_two
        if self.frequency > 0:
            frequency_bonus = self.frequency - 49
            frequency_bonus = frequency_bonus * (-1)
            frequency_bonus = frequency_bonus * 5 + 230
        self.combined_frequency = frequency_bonus + frequency_again
        return self.combined_frequency
    
    def __unicode__(self):
        return self.real_word

class WordMeanings(models.Model):
    word = models.ForeignKey(Words, related_name = "the_meanings")
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
    master_order = models.IntegerField(null = True)
    level = models.IntegerField(null = True)
    sub_level = models.IntegerField(null = True)

    def __unicode__(self):
        return self.name

class WordPos(models.Model):
    word = models.ForeignKey(Words, related_name="thepos")
    pos = models.CharField(max_length = 500)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    number_words_practiced_today = models.IntegerField(default = 0)
    words_practiced_today_time_marker = models.DateTimeField(auto_now_add = True)
    most_words_practiced_in_day = models.IntegerField(default = 0)
    total_words_reviewed_ever = models.IntegerField(default=0)
    total_correct_reviews = models.IntegerField(default=0)
    total_incorrect_reviews  = models.IntegerField(default=0)

# to do from client side esnd timezone adjustment, logic for when to make add and not add to practiced
    def update_words_practiced_today(self, timezone_adjustment):
        current_datetime = datetime.now() - timedelta(hours = timezone_adjustment)
        current_day = current_datetime.day

        if self.words_practied_today_time_marker.day != current_day:
            self.number_words_practiced_today = 0
        else:
            self.number_words_practiced_today += 1
            if self.number_words_practiced_today > self.most_words_practiced_in_day:
                self.most_words_practiced_in_day = self.number_words_practiced_today
        self.words_practied_today_time_marker = current_datetime
        return

    def update_total_reviews_result(self, correct):
        if correct:
            self.total_correct_reviews += 1
        else:
            self.total_incorrect_reviews += 1
        return

    def total_reviews_ever(self):
        total_reviews = self.total_correct_reviews + self.total_incorrect_reviews
        return total_reviews

    def percent_correct(self):
        percent_correct = 100 * (self.total_correct_reviews / self.total_reviews_ever())
        percent_correct = round(percent_correct, 1)
        return percent_correct 

    def check_if_new_day(self,timezone_adjustment):
        current_datetime = datetime.now() - timedelta(hours = timezone_adjustment)
        current_day = current_datetime.day

        if self.words_practied_today_time_marker.day != current_day:
            self.number_words_practiced_today = 0
        self.words_practied_today_time_marker = current_datetime    
        return    
    
    def __unicode__(self):
        return unicode(self.user)

class UserSets(models.Model):
    sets_fk = models.ForeignKey(Sets)
    user_profile_fk = models.ForeignKey(UserProfile)
    completion_status  = models.BooleanField(default = False)
    creation_time = models.DateTimeField("creation_time", auto_now_add=True)
        
# create corresponding user profile when user is created
from registration.signals import user_registered
def createUserProfile(sender, user, request, **kwargs):
    user_profile = UserProfile.objects.get_or_create(user=user)
    decks = Sets.objects.exclude(master_order__isnull=True)
    new_decks = []
    for deck in decks:
        new_user_deck = UserSets(sets_fk=deck, user_profile_fk=user_profile[0])
        new_decks.append(new_user_deck)
    UserSets.objects.bulk_create(new_decks)
        
user_registered.connect(createUserProfile)
    

class KnownKanji(models.Model):
    kanji_fk =  models.ForeignKey(Kanji, related_name = "kanji_fk", null = True)
    date_added = models.DateTimeField(auto_now_add = True)
    selected_kanji = models.BooleanField(default = False)
    user_profile = models.ManyToManyField(UserProfile)
    
    def __unicode__(self):
        return unicode(self.kanji)

class KnownWords(models.Model):
    words = models.ForeignKey(Words)
    user_profile = models.ForeignKey(UserProfile)
    date_added = models.DateTimeField(auto_now_add = True)
    tier_level = models.IntegerField()
    last_practiced = models.DateTimeField(blank = True)
    time_until_review = models.FloatField(null = True)
    times_answered_correct = models.IntegerField(default = 0)
    times_answered_wrong = models.IntegerField(default = 0)
    correct_percentage = models.FloatField(null = True)

    def set_initial_level(self):
        self.tier_level = 1
        random_multiplier = random.uniform(.95, 1.05)
        self.last_practiced = datetime.now()
        self.time_until_review = timedelta(hours = 3.5).total_seconds() * random_multiplier
        return

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

class SentenceOwner(models.Model):
    name = models.CharField(max_length = 50, default=' ', null=True)

    def __unicode__(self):
        return self.name

class Sentence(models.Model):
    japanese_sentence = models.TextField(null=True)
    english_sentence = models.TextField(null=True)
    words = models.ManyToManyField(Words)
    sentence_owner = models.ForeignKey(SentenceOwner, null=True)
    date_added = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    source_url = models.CharField(max_length = 70, null=True)
    source_id = models.PositiveIntegerField(null=True)
    comment_exists = models.BooleanField(default = False)
    audio = models.URLField(max_length=200, null=True)
    in_production = models.BooleanField(default = False)
