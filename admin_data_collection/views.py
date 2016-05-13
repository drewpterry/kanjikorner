# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import UserProfile, Sets, Words, Kanji, KnownKanji, KnownWords, Sentence, WordMeanings
from django.contrib.auth.models import User
from django.db import connection
import json
from django.core import serializers
from datetime import datetime, timedelta, date
from django.utils.timezone import utc
import time
from django.template.context_processors import csrf
from django.views.decorators.cache import cache_control
from django.views.generic import View
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from .forms import WordsForm, MeaningsForm, SentenceForm
from django.forms import modelformset_factory 
from django.forms import inlineformset_factory 
from manageset.models import Words, WordMeanings, Sentence, SentenceOwner
import pdb 


# Create your views here.
@staff_member_required
def index(request):
    return render(request, 'admin_data_collection/admin_dashboard.html', {"words":words}) 
  
@staff_member_required
def sentence_review(request):
    words = Words.objects.filter(jlpt_level = 5, id__lte=400)
    form_objects = []
    test_query = Words.objects.get(real_word = "お金")
    test_sentence = Sentence.objects.filter(words = test_query)
    sentence_object = Sentence.objects.get(id = 46349)
    for word in words:
        full_form = []
        word_form = WordsForm(instance=word)
        full_form.append(word_form)
        meaningset = modelformset_factory(WordMeanings, form=MeaningsForm, extra=4, max_num=8)
        meaningset= meaningset(queryset=WordMeanings.objects.filter(word=word))
        full_form.append(meaningset)
        sentence_formset = modelformset_factory(Sentence, form=SentenceForm)
        no_sentence_owner_object = SentenceOwner.objects.get(name=" ")
        sentence_formset = sentence_formset(queryset=Sentence.objects.filter(words=word).exclude(sentence_owner=no_sentence_owner_object))
        full_form.append(sentence_formset)
        form_objects.append(full_form)
        sentence_formset = modelformset_factory(Sentence, form=SentenceForm)
        for form in form_objects:
            for field in form[0]:
                pass
    return render(request, 'admin_data_collection/word_def_sentence_review.html', {"forms": form_objects} ) 

def save_sentence_review_form(request):
    return
 
@staff_member_required
def question_answer_screen(request):
    words = Words.objects.filter(jlpt_level = 5, id__lte=400)
    form_objects = []
    test_query = Words.objects.get(real_word = "お金")
    test_sentence = Sentence.objects.filter(words = test_query)
    sentence_object = Sentence.objects.get(id = 46349)
    for word in words:
        full_form = []
        word_form = WordsForm(instance=word)
        full_form.append(word_form)
        meaningset = modelformset_factory(WordMeanings, form=MeaningsForm, extra=4, max_num=8)
        meaningset= meaningset(queryset=WordMeanings.objects.filter(word=word))
        full_form.append(meaningset)
        sentence_formset = modelformset_factory(Sentence, form=SentenceForm)
        no_sentence_owner_object = SentenceOwner.objects.get(name=" ")
        sentence_formset = sentence_formset(queryset=Sentence.objects.filter(words=word).exclude(sentence_owner=no_sentence_owner_object))
        full_form.append(sentence_formset)
        form_objects.append(full_form)
        sentence_formset = modelformset_factory(Sentence, form=SentenceForm)
        for form in form_objects:
            for field in form[0]:
                pass
    return render(request, 'admin_data_collection/word_question_answers.html', {"forms": form_objects} ) 
