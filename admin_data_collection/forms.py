from django.db import models
from django.forms import ModelForm, BaseInlineFormSet
from django import forms
from manageset.models import Words, WordMeanings, Sentence


class WordsForm(ModelForm):
    class Meta:
        model = Words 
        fields = ('real_word', 'hiragana', 'frequency_thousand', 'jlpt_level', 'reviewed', 'master_order')
        widgets = {
            'real_word': forms.TextInput(attrs={'class': 'form-control', 'label':''}),
            'hiragana': forms.TextInput(attrs={'class': 'form-control'}),
            'frequency_thousand': forms.NumberInput(attrs={'class': 'form-control'}),
            'jlpt_level': forms.TextInput(attrs={'class': 'form-control'}),
            'reviewed': forms.TextInput(attrs={'class': 'form-control'}),
            'master_order': forms.NumberInput(attrs={'class': 'form-control'}),
        }            
        labels = {
            'real_word': '',
        }

class MeaningsForm(ModelForm):
    class Meta:
        model = WordMeanings 
        fields = ('meaning',)
        widgets = {
            'meaning': forms.TextInput(attrs={'class': 'form-control'}),
        }            
        labels = {
            'meaning': '',
        }

class SentenceForm(ModelForm):
    class Meta:
        model = Sentence 
        # fields = ('japanese_sentence', 'english_sentence','words')
        fields = ('japanese_sentence', 'english_sentence')
        widgets = {
            'japanese_sentence': forms.TextInput(attrs={'class': 'form-control'}),
            'english_sentence': forms.TextInput(attrs={'class': 'form-control'}),
            # 'words': forms.TextInput(attrs={'class': 'form-control'}),
        }            
        labels = {
            'japanese_sentence': '',
            'english_sentence': '',
        }

