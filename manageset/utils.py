from manageset.models import UserProfile, Sets, Words, Kanji, KnownWords, AnalyticsLog
from django.contrib.auth.models import User
from datetime import datetime, timedelta, time, date
from django.template.context_processors import csrf
from django.utils.timezone import utc
from django.db.models import F
import copy

def update_word_queue(user):
    words = (KnownWords.objects.filter(
        user_profile = user.userprofile,
        tier_level__lte = 7)
        .exclude(tier_level = 0)
        .exclude(time_until_review = None)
        .order_by('time_until_review')
        .select_related('words')
        )
    if words.exists():
        now = datetime.utcnow().replace(tzinfo=utc)
        last_practiced = words[0].last_practiced
        difference = now - last_practiced
        difference = difference.total_seconds()
                
        words.update(last_practiced = now, time_until_review = F('time_until_review') - difference)
    return

def update_analytics_log(user):
    words_reviewed = user.userprofile.total_reviews_ever()
    log, created = AnalyticsLog.objects.update_or_create(user_profile = user.userprofile, last_modified = date.today(), defaults={'words_reviewed_count': words_reviewed})
    if created:
        try:
            most_recent_log = AnalyticsLog.objects.filter(user_profile = user.userprofile, last_modified__lt = date.today()).latest('last_modified')
            # yesterday = date.today() - timedelta(days=1)
            # if most_recent_log.last_modified != yesterday:
            x = 1
            new_day = date.today() - timedelta(days=x) 
            while most_recent_log.last_modified != new_day:
                log_copy = copy.copy(most_recent_log)
                log_copy.pk = None
                log_copy.last_modified = new_day 
                log_copy.save()
                x += 1
                new_day = date.today() - timedelta(days=x) 
        except AnalyticsLog.DoesNotExist:
            return
    return
