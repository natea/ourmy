# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SharingCampaign'
        db.create_table('sharing_sharingcampaign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ourmy_app.Campaign'], unique=True)),
            ('post_text', self.gf('django.db.models.fields.CharField')(default='Check this out and spread the word!', max_length=120)),
            ('long_url', self.gf('django.db.models.fields.URLField')(default='http://www.youtube.com/user/CrewTide/featured?great', max_length=200)),
        ))
        db.send_create_signal('sharing', ['SharingCampaign'])

        # Adding model 'SharingCampaignUser'
        db.create_table('sharing_sharingcampaignuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sharing_campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sharing.SharingCampaign'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('sharable_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('sharing', ['SharingCampaignUser'])

        # Adding model 'SharingAction'
        db.create_table('sharing_sharingaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ourmy_app.Action'], unique=True)),
            ('social_network', self.gf('django.db.models.fields.CharField')(default='FB', max_length=2)),
            ('post_or_click', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('sharing', ['SharingAction'])

        # Adding model 'SharingUserAction'
        db.create_table('sharing_sharinguseraction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('sharing_action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sharing.SharingAction'])),
        ))
        db.send_create_signal('sharing', ['SharingUserAction'])


    def backwards(self, orm):
        # Deleting model 'SharingCampaign'
        db.delete_table('sharing_sharingcampaign')

        # Deleting model 'SharingCampaignUser'
        db.delete_table('sharing_sharingcampaignuser')

        # Deleting model 'SharingAction'
        db.delete_table('sharing_sharingaction')

        # Deleting model 'SharingUserAction'
        db.delete_table('sharing_sharinguseraction')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'ourmy_app.action': {
            'Meta': {'object_name': 'Action'},
            'api_call': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ourmy_app.Campaign']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 10, 0, 0)', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_checked': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 10, 0, 0)'}),
            'logo_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'start_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 10, 0, 0)', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'ourmy_app.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'api_call': ('django.db.models.fields.CharField', [], {'default': "'sharing.get_actions_for_campaign'", 'max_length': '500'}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 10, 0, 0)', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '250', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'sharing.sharingaction': {
            'Meta': {'object_name': 'SharingAction'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ourmy_app.Action']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_or_click': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_network': ('django.db.models.fields.CharField', [], {'default': "'FB'", 'max_length': '2'})
        },
        'sharing.sharingcampaign': {
            'Meta': {'object_name': 'SharingCampaign'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ourmy_app.Campaign']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_url': ('django.db.models.fields.URLField', [], {'default': "'http://www.youtube.com/user/CrewTide/featured?great'", 'max_length': '200'}),
            'post_text': ('django.db.models.fields.CharField', [], {'default': "'Check this out and spread the word!'", 'max_length': '120'})
        },
        'sharing.sharingcampaignuser': {
            'Meta': {'object_name': 'SharingCampaignUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sharable_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'sharing_campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sharing.SharingCampaign']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'sharing.sharinguseraction': {
            'Meta': {'object_name': 'SharingUserAction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sharing_action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sharing.SharingAction']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['sharing']