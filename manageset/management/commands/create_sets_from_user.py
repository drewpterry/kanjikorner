# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from manageset.models import UserProfile, Sets, Words, Kanji, KnownKanji, KnownWords
from datetime import datetime, timedelta, date
import csv
import sys
import os
class Command(BaseCommand):
    help = 'create master stacks from user'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int)

    def _create_stacks_and_order(self, user_id):
        self.delete_master_stacks()
        words = self.get_user_word_list(user_id)
        self.assign_word_master_order(words)
        # TODO add back later or move into different place
        # self.create_stacks_from_master_order()
        print "complete!"
        
    def get_user_word_list(self, user_id):
        user = UserProfile.objects.get(user_id = user_id)
        word_list = KnownWords.objects.filter(user_profile = user).order_by('date_added')
        print "got word list" 
        return word_list 

    def assign_word_master_order(self, words):
        Words.objects.all().update(master_order = None)
        count = 0
        for each in words:
          count += 1
          each.words.master_order = count
          each.words.save()
        print "master order saved"

    def create_stacks_from_master_order(self):
        print "creating stacks..." 
        words = Words.objects.exclude(master_order = None).order_by("master_order")
        count = 0
        stacks_created = 0
        level = 1
        sub_level = 1
        words_to_add = []

        for word in words:
            count += 1
            words_to_add.append(word)
            if count % 5 == 0: 
                master_order_number = count / 5
                newset = Sets(
                    name = master_order_number, 
                    pub_date = datetime.now(), 
                    times_practiced = 0, 
                    level = level, 
                    sub_level = sub_level, 
                    master_order = master_order_number)
                newset.save()
                newset.words.add(*words_to_add)
                words_to_add = []
                stacks_created += 1
                sub_level += 1
                if stacks_created % 20 == 0 and stacks_created != 0:
                    level += 1
                    print "here", level
                    sub_level = 1
        print "stacks created"

    def delete_master_stacks(self):
        stacks = Sets.objects.exclude(master_order = None)
        stacks.delete()

    def handle(self, *args, **options):
        self._create_stacks_and_order(options['user_id'])       
    
