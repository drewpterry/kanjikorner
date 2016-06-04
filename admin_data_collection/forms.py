from django.db import models
from django.forms import ModelForm
from django import forms
from manageset.models import Words, WordMeanings, Sentence


class WordsForm(ModelForm):
    class Meta:
        model = Words 
        fields = ('id', 'real_word', 'hiragana', 'frequency_thousand', 'jlpt_level')
        widgets = {
            # 'id': forms.TextInput(attrs={'read-only': 'read-only'}),
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
            'real_word': forms.TextInput(attrs={'class': 'form-control'}),
            'hiragana': forms.TextInput(attrs={'class': 'form-control'}),
            'frequency_thousand': forms.NumberInput(attrs={'class': 'form-control'}),
            'jlpt_level': forms.TextInput(attrs={'class': 'form-control'}),
        }            

class MeaningsForm(ModelForm):
    class Meta:
        model = WordMeanings 
        fields = ('id','meaning',)
        widgets = {
                'meaning': forms.TextInput(attrs={'class': 'form-control', 'name': "testing"}),
        }            

class SentenceForm(ModelForm):
    class Meta:
        model = Sentence 
        fields = ('id', 'japanese_sentence', 'english_sentence',)
        widgets = {
            'japanese_sentence': forms.TextInput(attrs={'class': 'form-control'}),
            'english_sentence': forms.TextInput(attrs={'class': 'form-control'}),
        }            
