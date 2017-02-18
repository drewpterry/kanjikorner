from django.test import TestCase
from django.core.management import call_command
from django.conf import settings
from manageset.models import *

class ManagestModelTest(TestCase):
    def setUp(self):
        # call_command('loaddata', 'testdb.json', verbosity=0)
        self.user = User.objects.create_user(username='testuser', password='12345') 
        self.user.save() 
        self.user_profile, created = UserProfile.objects.get_or_create(user=self.user)
        self.user_profile.save()
        self.analyticsLog = AnalyticsLog.objects.get_or_create(self.user) 
        self.analyticsLog.save()

    def test_analyticslog_model(self):
        self.analyticsLog.update_on_stack_complete()
        self.assertEqual(self.analyticsLog.words_studied_count, 5)
        self.assertEqual(self.analyticsLog.words_studied_count_today, 5)

        self.analyticsLog.update_correct_or_incorrect(True)
        self.assertEqual(self.analyticsLog.total_correct_reviews, 1)
        self.analyticsLog.update_correct_or_incorrect(False)
        self.assertEqual(self.analyticsLog.total_incorrect_reviews, 1)

        self.analyticsLog.percent_correct()
        self.assertEqual(self.analyticsLog.percent_correct(), 0)

        self.analyticsLog.update_words_reviewed()
        self.analyticsLog.update_words_reviewed()
        self.assertEqual(self.analyticsLog.words_reviewed_count, 2)
        self.assertEqual(self.analyticsLog.words_reviewed_count_today, 2)

        self.analyticsLog.percent_correct()
        self.assertEqual(self.analyticsLog.percent_correct(), 50)
        
        self.analyticsLog.reset_daily_values()
        self.assertEqual(self.analyticsLog.words_studied_count_today, 0)

    # def progress_percent(self):
        # master_word_count = Words.objects.filter(master_order__gt=0).count()
        # progress_percent = 100 * (self.words_studied_count / master_word_count)
        # progress_percent = round(progress_percent, 1)
        # return progress_percent 

