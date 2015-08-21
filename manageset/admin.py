from django.contrib import admin
from manageset.models import Sets, Words, UserProfile, Kanji, WordMeanings

# Register your models here.

# class WordsInline(admin.TabularInline):
#     model = Words
#     #adds the number of choice additions you can add at once
#     extra = 3

# class SetsInline(admin.TabularInline):
#     model = Sets

class SetsAdmin(admin.ModelAdmin):
    fields = ('name','description', 'pub_date', 'words', 'kanji')
    # inlines = [WordsInline]

class MeaningsInline(admin.TabularInline):
    model = WordMeanings

class WordsAdmin(admin.ModelAdmin):
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
    extra = 5
    
    # def get_kanji(self, obj):
#         return "\n".join([p.kanji_name for p in obj.kanji.all()])


    
class KanjiAdmin(admin.ModelAdmin):
    fields = ('kanji_name', 'kanji_meaning','readings', 'strokes', 'grade')
    extra = 5
    
class UserProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'user_sets')   
    # inlines = [SetsInline]     


admin.site.register(Sets, SetsAdmin)
admin.site.register(Words, WordsAdmin)
admin.site.register(Kanji, KanjiAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(WordMeanings, WordMeaningsAdmin)
