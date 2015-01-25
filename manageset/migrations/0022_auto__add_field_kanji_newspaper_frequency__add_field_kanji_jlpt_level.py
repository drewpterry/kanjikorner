# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Kanji.newspaper_frequency'
        db.add_column(u'manageset_kanji', 'newspaper_frequency',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Kanji.jlpt_level'
        db.add_column(u'manageset_kanji', 'jlpt_level',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Kanji.newspaper_frequency'
        db.delete_column(u'manageset_kanji', 'newspaper_frequency')

        # Deleting field 'Kanji.jlpt_level'
        db.delete_column(u'manageset_kanji', 'jlpt_level')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'manageset.kanji': {
            'Meta': {'object_name': 'Kanji'},
            'grade': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jlpt_level': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'kanji_meaning': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'kanji_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'newspaper_frequency': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'readings': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'strokes': ('django.db.models.fields.IntegerField', [], {})
        },
        u'manageset.knownkanji': {
            'Meta': {'object_name': 'KnownKanji'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kanji': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['manageset.Kanji']", 'symmetrical': 'False'}),
            'number_of_chosen_words': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'selected_kanji': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_profile': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['manageset.UserProfile']", 'symmetrical': 'False'})
        },
        u'manageset.knownwords': {
            'Meta': {'object_name': 'KnownWords'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_practiced': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'tier_level': ('django.db.models.fields.IntegerField', [], {}),
            'time_until_review': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['manageset.UserProfile']"}),
            'words': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['manageset.Words']"})
        },
        u'manageset.sets': {
            'Meta': {'object_name': 'Sets'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kanji': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['manageset.Kanji']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'times_practiced': ('django.db.models.fields.IntegerField', [], {}),
            'words': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['manageset.Words']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'manageset.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'user_sets': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['manageset.Sets']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'manageset.wordmeanings': {
            'Meta': {'object_name': 'WordMeanings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meaning': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['manageset.Words']"})
        },
        u'manageset.words': {
            'Meta': {'object_name': 'Words'},
            'duplicate_word': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frequency': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'frequency_two': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_index': 'True'}),
            'hiragana': ('django.db.models.fields.CharField', [], {'max_length': '301'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kanji': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['manageset.Kanji']", 'symmetrical': 'False', 'blank': 'True'}),
            'meaning': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'part_of_speech': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'real_word': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['manageset']