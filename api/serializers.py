from django.contrib.auth.models import User, Group
from manageset.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class WordPosSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordPos
        fields = ('pos',)

class WordMeaningsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordMeanings 
        fields = ('meaning',)

class WordsSerializer(serializers.ModelSerializer):
    kanji = serializers.StringRelatedField(many=True)
    meanings = WordMeaningsSerializer(source='the_meanings', read_only=True, many=True)
    pos = WordPosSerializer(source='thepos', read_only=True, many=True)
    
    class Meta:
        model = Words 
        fields = ('real_word', 'meanings', 'kanji', 'hiragana', 'pos', 'master_order')

class SetsSerializer(serializers.HyperlinkedModelSerializer):
    words = WordsSerializer(many=True, read_only=True)
    class Meta:
        model = Sets 
        fields = ('id', 'name', 'level', 'sub_level', 'words', 'master_order')

class SetsSerializerWithoutWords(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sets 
        fields = ('id', 'name', 'level', 'sub_level', 'master_order')

class UserSetsSerializer(serializers.ModelSerializer):
    sets_fk = SetsSerializerWithoutWords(read_only=True)
    class Meta:
        model = UserSets 
        fields = ('sets_fk', 'completion_status')

class KnownWordsSerializer(serializers.HyperlinkedModelSerializer):
    words = WordsSerializer(read_only=True)
    class Meta:
        model = KnownWords 
        fields = ('id', 'words', 'tier_level')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    total_reviews_ever = serializers.ReadOnlyField()
    percent_correct = serializers.ReadOnlyField()
    class Meta:
        model = UserProfile 
        fields = ('id', 'number_words_practiced_today', 'most_words_practiced_in_day', 'total_reviews_ever', 'percent_correct')
