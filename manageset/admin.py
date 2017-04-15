from django.contrib import admin
from manageset.models import Sets, Words, UserProfile, Kanji, WordMeanings, Sentence, WordQuestion
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin(ImportExportModelAdmin):
    list_display = (
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'date_joined',
            'is_staff',
            'userprofile_foo'
            )

    def userprofile_foo(self, x):
            return x.userprofile.most_words_practiced_in_day
    resource_class = UserResource
           
class SetsAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            'description',
            'master_order',
            'level',
            'sub_level'
            )
    list_editable = (
            'name',
            'description',
            'master_order',
            'level',
            'sub_level'
            )
    fields = (
            'name',
            'description',
            'words',
            'kanji',
            'master_order',
            'level',
            'sub_level'
            )

class MeaningsInline(admin.TabularInline):
    model = WordMeanings

class WordQuestionInline(admin.TabularInline):
    model = WordQuestion

class WordsResource(resources.ModelResource):
    class Meta:
        model = Words

class WordsAdmin(ImportExportModelAdmin):
    list_display = (
            'id',
            'master_order',
            'real_word',
            'meaning',
            'hiragana',
            'combined_frequency',
            'frequency_thousand',
            'published',
            'master_order'
            )
    list_editable = (
            'combined_frequency',
            'frequency_thousand',
            'published',
            'master_order'
            )
    fields = (
            'real_word',
            'meaning',
            'hiragana',
            'frequency',
            'frequency_two',
            'combined_frequency',
            'frequency_thousand',
            'part_of_speech',
            'published',
            'duplicate_word',
            'master_order',
            'kanji'
            )
    list_filter = ('published',)
    inlines = [
        MeaningsInline,
        WordQuestionInline,
    ]
    search_fields = ['real_word', 'meaning', 'hiragana']
    ordering = ['-combined_frequency']
    resource_class = WordsResource
    
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'most_words_practiced_in_day')   
    fields = ('user', 'user_sets', 'most_words_practiced_in_day')   

class KanjiResource(resources.ModelResource):
    class Meta:
        model = Kanji

class KanjiAdmin(ImportExportModelAdmin):
    fields = ('kanji_name', 'kanji_meaning','readings', 'strokes', 'grade', 'master_order')
    list_display = (
            'kanji_name',
            'kanji_meaning',
            'readings',
            'strokes',
            'on_kun_readings',
            'grade',
            'jlpt_level',
            'newspaper_frequency',
            'jinmeiyo',
            'twitter_frequency',
            'aozora_frequency',
            'news_frequency',
            'wikipedia_frequency',
            'master_order'
            )
    list_editable = ('kanji_meaning', 'master_order')
    list_filter = ('jlpt_level',)
    search_fields = ('kanji_name', 'kanji_meaning')
    ordering = ['jlpt_level', 'grade', 'newspaper_frequency']
    resource_class = KanjiResource
    pass


class SentenceResource(resources.ModelResource):
    class Meta:
        model = Sentence

class SentenceAdmin(ImportExportModelAdmin):
    def get_owner(self, obj):
        return obj.sentence_owner.name

    fields = ('japanese_sentence', 'english_sentence', 'sentence_owner', 'source_url', 'comment_exists', 'audio',)
    list_display = ('japanese_sentence', 'english_sentence', 'sentence_owner', 'source_url', 'comment_exists', 'audio',)
    search_fields = ('japanese_sentence', 'english_sentence', 'sentence_owner__name')
    list_filter = ('sentence_owner',)
    resource_class = SentenceResource
    pass

admin.site.register(Sets, SetsAdmin)
admin.site.register(Words, WordsAdmin)
admin.site.register(Kanji, KanjiAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Sentence, SentenceAdmin)
