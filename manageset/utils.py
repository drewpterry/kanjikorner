from manageset.models import UserProfile, Sets, Words, Kanji, KnownWords, AnalyticsLog
from django.contrib.auth.models import User
from datetime import datetime, timedelta, time, date
from django.template.context_processors import csrf
from django.utils.timezone import utc
from django.db.models import F

# TODO probably can move into a model manager and simply delete this file
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
