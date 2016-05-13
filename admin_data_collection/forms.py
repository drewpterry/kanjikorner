from django.db import models
from django.forms import ModelForm
from django import forms
from manageset.models import Words, WordMeanings, Sentence


class WordsForm(ModelForm):
    class Meta:
        model = Words 
        fields = ('real_word', 'hiragana', 'frequency_thousand', 'jlpt_level')
        widgets = {
            'real_word': forms.TextInput(attrs={'class': 'form-control'}),
            'hiragana': forms.TextInput(attrs={'class': 'form-control'}),
            'frequency_thousand': forms.NumberInput(attrs={'class': 'form-control'}),
            'jlpt_level': forms.TextInput(attrs={'class': 'form-control'}),
        }            

class MeaningsForm(ModelForm):
    meaning = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': "testing"}), label='')
    class Meta:
        model = WordMeanings 
        fields = ('meaning',)
        # widgets = {
                # 'meaning': forms.TextInput(attrs={'class': 'form-control', 'name': "testing"}),
        # }            

class SentenceForm(ModelForm):
    japanese_sentence = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': "testing"}), label='')
    english_sentence = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': "testing"}), label='')
    in_production= forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'pull-right'}), label='')
    class Meta:
        model = Sentence 
        fields = ('japanese_sentence', 'english_sentence', 'in_production')
        widgets = {
            # 'japanese_sentence': forms.TextInput(attrs={'class': 'form-control'}),
            # 'english_sentence': forms.TextInput(attrs={'class': 'form-control'}),
            # 'in_production': forms.CheckboxInput(attrs={'class': 'pull-right'}),

        }            
