from django.shortcuts import render
from django.conf.urls import patterns, url
from admin_data_collection import views

urlpatterns = [
            url(r'^$', views.index, name='data_collection_index'),
            url('word-sentence-review', views.sentence_review, name='sentence_review_screen'),
            url('word-questions', views.question_answer_screen, name='question_answer_screen'),
            ]
