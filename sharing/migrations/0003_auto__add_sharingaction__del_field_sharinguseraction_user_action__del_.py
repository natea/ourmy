# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SharingAction'
        db.create_table('sharing_sharingaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ourmy_app.Action'], unique=True)),
            ('social_network', self.gf('django.db.models.fields.CharField')(default='FB', max_length=2)),
            ('post_or_clicked', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('sharing', ['SharingAction'])

        # Deleting field 'SharingUserAction.user_action'
        db.delete_column('sharing_sharinguseraction', 'user_action_id')

        # Deleting field 'SharingUserAction.social_network'
        db.delete_column('sharing_sharinguseraction', 'social_network')

        # Deleting field 'SharingUserAction.last_checked'
        db.delete_column('sharing_sharinguseraction', 'last_checked')

        # Deleting field 'SharingUserAction.post_or_clicked'
        db.delete_column('sharing_sharinguseraction', 'post_or_clicked')

        # Adding field 'SharingUserAction.user'
        db.add_column('sharing_sharinguseraction', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'SharingUserAction.sharing_action'
        db.add_column('sharing_sharinguseraction', 'sharing_action',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['sharing.SharingAction']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'SharingAction'
        db.delete_table('sharing_sharingaction')

        # Adding field 'SharingUserAction.user_action'
        db.add_column('sharing_sharinguseraction', 'user_action',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['ourmy_app.UserAction']),
                      keep_default=False)

        # Adding field 'SharingUserAction.social_network'
        db.add_column('sharing_sharinguseraction', 'social_network',
                      self.gf('django.db.models.fields.CharField')(default='FB', max_length=2),
                      keep_default=False)

        # Adding field 'SharingUserAction.last_checked'
        db.add_column('sharing_sharinguseraction', 'last_checked',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default='', blank=True),
                      keep_default=False)

        # Adding field 'SharingUserAction.post_or_clicked'
        db.add_column('sharing_sharinguseraction', 'post_or_clicked',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'SharingUserAction.user'
        db.delete_column('sharing_sharinguseraction', 'user_id')

        # Deleting field 'SharingUserAction.sharing_action'
        db.delete_column('sharing_sharinguseraction', 'sharing_action_id')


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
            'end_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_checked': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'logo_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'start_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'ourmy_app.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'api_call': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
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
            'post_or_clicked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_network': ('django.db.models.fields.CharField', [], {'default': "'FB'", 'max_length': '2'})
        },
        'sharing.sharingcampaign': {
            'Meta': {'object_name': 'SharingCampaign'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ourmy_app.Campaign']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_url': ('django.db.models.fields.URLField', [], {'default': "'http://zoomtilt.com'", 'max_length': '200'}),
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