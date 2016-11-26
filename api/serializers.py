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

# class WordMeaningsSerializer(serializers.HyperlinkedModelSerializer):
    # class Meta:
        # model = WordMeanings 
        # fields = ('meaning', 'master_order')

class WordsSerializer(serializers.HyperlinkedModelSerializer):
    word_meanings = serializers.StringRelatedField(many=True)
    class Meta:
        model = Words 
        fields = ('word_meanings', 'master_order')

class SetsSerializer(serializers.HyperlinkedModelSerializer):
    words = WordsSerializer(many=True, read_only = True)
    class Meta:
        model = Sets 
        fields = ('name', 'level', 'sub_level', 'words', 'master_order')
