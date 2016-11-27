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
    words = WordsSerializer(many=True, read_only = True)
    class Meta:
        model = Sets 
        fields = ('id', 'name', 'level', 'sub_level', 'words', 'master_order')
