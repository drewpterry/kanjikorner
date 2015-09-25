from django.contrib import admin
from manageset.models import Sets, Words, UserProfile, Kanji, WordMeanings
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# class WordsInline(admin.TabularInline):
#     model = Words
#     #adds the number of choice additions you can add at once
#     extra = 3

# class SetsInline(admin.TabularInline):
#     model = Sets


class UserResource(resources.ModelResource):

    class Meta:
        model = User

class UserAdmin(ImportExportModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff', 'userprofile_foo')
    def userprofile_foo(self, x):
            return x.userprofile.most_words_practiced_in_day
    resource_class = UserResource
           
# UserAdmin.list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')

class SetsAdmin(admin.ModelAdmin):
    fields = ('name','description', 'pub_date', 'words', 'kanji')
    # inlines = [WordsInline]

class MeaningsInline(admin.TabularInline):
    model = WordMeanings

class WordsResource(resources.ModelResource):

    class Meta:
        model = Words

class WordsAdmin(ImportExportModelAdmin):
    # ef get_kanji(self, obj):
#         return "\n".join([p.kanji_name for p in obj.kanji.all()])
    list_display = ('real_word' ,'meaning', 'hiragana', 'combined_frequency', 'frequency_thousand', 'published')
    list_editable = ('combined_frequency', 'frequency_thousand', 'published')
    fields = ('real_word', 'meaning', 'hiragana', 'kanji', 'frequency', 'frequency_two', 'combined_frequency', 'frequency_thousand','part_of_speech','published','duplicate_word')
    list_filter = ('published',)
    inlines = [
        MeaningsInline,
    ]
    search_fields = ['real_word', 'meaning', 'hiragana']
    ordering = ['-combined_frequency']
    resource_class = WordsResource
    
    # def get_kanji(self, obj):
#         return "\n".join([p.kanji_name for p in obj.kanji.all()])

    
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'most_words_practiced_in_day')   
    fields = ('user', 'user_sets', 'most_words_practiced_in_day')   
    # inlines = [SetsInline]     

class KanjiResource(resources.ModelResource):

    class Meta:
        model = Kanji

class KanjiAdmin(ImportExportModelAdmin):
    fields = ('kanji_name', 'kanji_meaning','readings', 'strokes', 'grade')
    list_display = ('kanji_name', 'kanji_meaning','readings', 'strokes', 'on_kun_readings', 'grade', 'jlpt_level', 'newspaper_frequency', 'jinmeiyo')
    list_editable = ('kanji_meaning',)
    list_filter = ('jlpt_level',)
    search_fields = ('kanji_name', 'kanji_meaning')
    ordering = ['jlpt_level', 'grade', 'newspaper_frequency']
    resource_class = KanjiResource
    pass

admin.site.register(Sets, SetsAdmin)
admin.site.register(Words, WordsAdmin)
admin.site.register(Kanji, KanjiAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# admin.site.register(WordMeanings, WordMeaningsAdmin)