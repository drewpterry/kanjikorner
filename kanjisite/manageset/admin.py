from django.contrib import admin
from manageset.models import Sets, Words, UserProfile, Kanji

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

class WordsAdmin(admin.ModelAdmin):
    fields = ('real_word', 'meaning', 'hiragana', 'kanji')
    
class KanjiAdmin(admin.ModelAdmin):
    fields = ('kanji_name', 'kanji_meaning','readings', 'strokes', 'grade')
    
class UserProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'user_sets')   
    # inlines = [SetsInline]     


admin.site.register(Sets, SetsAdmin)
admin.site.register(Words, WordsAdmin)
admin.site.register(Kanji, KanjiAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
