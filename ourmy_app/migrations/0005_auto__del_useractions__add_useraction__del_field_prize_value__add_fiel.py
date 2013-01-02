# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UserActions'
        db.delete_table('ourmy_app_useractions')

        # Adding model 'UserAction'
        db.create_table('ourmy_app_useraction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ourmy_app.Action'])),
        ))
        db.send_create_signal('ourmy_app', ['UserAction'])

        # Deleting field 'Prize.value'
        db.delete_column('ourmy_app_prize', 'value')

        # Adding field 'Prize.video_url'
        db.add_column('ourmy_app_prize', 'video_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Prize.dollar_value'
        db.add_column('ourmy_app_prize', 'dollar_value',
                      self.gf('django.db.models.fields.DecimalField')(default=10, max_digits=6, decimal_places=2),
                      keep_default=False)

        # Adding field 'Prize.points_value'
        db.add_column('ourmy_app_prize', 'points_value',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)

        # Adding field 'Prize.how_many'
        db.add_column('ourmy_app_prize', 'how_many',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Prize.place'
        db.add_column('ourmy_app_prize', 'place',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Prize.chance'
        db.add_column('ourmy_app_prize', 'chance',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Action.points_per_click'
        db.delete_column('ourmy_app_action', 'points_per_click')

        # Deleting field 'Action.social_network'
        db.delete_column('ourmy_app_action', 'social_network')

        # Deleting field 'Action.points_to_post'
        db.delete_column('ourmy_app_action', 'points_to_post')

        # Deleting field 'Action.start_on'
        db.delete_column('ourmy_app_action', 'start_on')

        # Deleting field 'Action.text'
        db.delete_column('ourmy_app_action', 'text')

        # Deleting field 'Action.end_on'
        db.delete_column('ourmy_app_action', 'end_on')

        # Adding field 'Action.title'
        db.add_column('ourmy_app_action', 'title',
                      self.gf('django.db.models.fields.CharField')(default='?', max_length=100),
                      keep_default=False)

        # Adding field 'Action.description'
        db.add_column('ourmy_app_action', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Action.logo_image'
        db.add_column('ourmy_app_action', 'logo_image',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Action.video_url'
        db.add_column('ourmy_app_action', 'video_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Action.points'
        db.add_column('ourmy_app_action', 'points',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Action.start_at'
        db.add_column('ourmy_app_action', 'start_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Action.end_at'
        db.add_column('ourmy_app_action', 'end_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Action.api_call'
        db.add_column('ourmy_app_action', 'api_call',
                      self.gf('django.db.models.fields.CharField')(default='?', max_length=500),
                      keep_default=False)

        # Adding field 'Action.last_checked'
        db.add_column('ourmy_app_action', 'last_checked',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Deleting field 'Campaign.long_url'
        db.delete_column('ourmy_app_campaign', 'long_url')

        # Adding field 'Campaign.video_url'
        db.add_column('ourmy_app_campaign', 'video_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Deleting field 'UserProfile.id'
        db.delete_column('ourmy_app_userprofile', 'id')

        # Deleting field 'UserProfile.user'
        db.delete_column('ourmy_app_userprofile', 'user_id')

        # Adding field 'UserProfile.singlyprofile_ptr'
        db.add_column('ourmy_app_userprofile', 'singlyprofile_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['singly.SinglyProfile'], unique=True, primary_key=True),
                      keep_default=False)

        # Adding field 'UserProfile.singly_profile'
        db.add_column('ourmy_app_userprofile', 'singly_profile',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='OurmyUserProfile', unique=True, to=orm['singly.SinglyProfile']),
                      keep_default=False)

        # Deleting field 'CampaignUser.stats'
        db.delete_column('ourmy_app_campaignuser', 'stats')

        # Deleting field 'CampaignUser.bitly_url'
        db.delete_column('ourmy_app_campaignuser', 'bitly_url')

        # Adding field 'CampaignUser.api_call'
        db.add_column('ourmy_app_campaignuser', 'api_call',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'UserActions'
        db.create_table('ourmy_app_useractions', (
            ('action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ourmy_app.Action'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('ourmy_app', ['UserActions'])

        # Deleting model 'UserAction'
        db.delete_table('ourmy_app_useraction')

        # Adding field 'Prize.value'
        db.add_column('ourmy_app_prize', 'value',
                      self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=6, decimal_places=2),
                      keep_default=False)

        # Deleting field 'Prize.video_url'
        db.delete_column('ourmy_app_prize', 'video_url')

        # Deleting field 'Prize.dollar_value'
        db.delete_column('ourmy_app_prize', 'dollar_value')

        # Deleting field 'Prize.points_value'
        db.delete_column('ourmy_app_prize', 'points_value')

        # Deleting field 'Prize.how_many'
        db.delete_column('ourmy_app_prize', 'how_many')

        # Deleting field 'Prize.place'
        db.delete_column('ourmy_app_prize', 'place')

        # Deleting field 'Prize.chance'
        db.delete_column('ourmy_app_prize', 'chance')

        # Adding field 'Action.points_per_click'
        db.add_column('ourmy_app_action', 'points_per_click',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Action.social_network'
        db.add_column('ourmy_app_action', 'social_network',
                      self.gf('django.db.models.fields.CharField')(default='facebook', max_length=100),
                      keep_default=False)

        # Adding field 'Action.points_to_post'
        db.add_column('ourmy_app_action', 'points_to_post',
                      self.gf('django.db.models.fields.IntegerField')(default=10),
                      keep_default=False)

        # Adding field 'Action.start_on'
        db.add_column('ourmy_app_action', 'start_on',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Action.text'
        db.add_column('ourmy_app_action', 'text',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Action.end_on'
        db.add_column('ourmy_app_action', 'end_on',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Deleting field 'Action.title'
        db.delete_column('ourmy_app_action', 'title')

        # Deleting field 'Action.description'
        db.delete_column('ourmy_app_action', 'description')

        # Deleting field 'Action.logo_image'
        db.delete_column('ourmy_app_action', 'logo_image')

        # Deleting field 'Action.video_url'
        db.delete_column('ourmy_app_action', 'video_url')

        # Deleting field 'Action.points'
        db.delete_column('ourmy_app_action', 'points')

        # Deleting field 'Action.start_at'
        db.delete_column('ourmy_app_action', 'start_at')

        # Deleting field 'Action.end_at'
        db.delete_column('ourmy_app_action', 'end_at')

        # Deleting field 'Action.api_call'
        db.delete_column('ourmy_app_action', 'api_call')

        # Deleting field 'Action.last_checked'
        db.delete_column('ourmy_app_action', 'last_checked')

        # Adding field 'Campaign.long_url'
        db.add_column('ourmy_app_campaign', 'long_url',
                      self.gf('django.db.models.fields.URLField')(default='http://zoomtilt.com', max_length=200),
                      keep_default=False)

        # Deleting field 'Campaign.video_url'
        db.delete_column('ourmy_app_campaign', 'video_url')


        # User chose to not deal with backwards NULL issues for 'UserProfile.id'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.id' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'UserProfile.user'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.user' and its values cannot be restored.")
        # Deleting field 'UserProfile.singlyprofile_ptr'
        db.delete_column('ourmy_app_userprofile', 'singlyprofile_ptr_id')

        # Deleting field 'UserProfile.singly_profile'
        db.delete_column('ourmy_app_userprofile', 'singly_profile_id')

        # Adding field 'CampaignUser.stats'
        db.add_column('ourmy_app_campaignuser', 'stats',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=400, blank=True),
                      keep_default=False)

        # Adding field 'CampaignUser.bitly_url'
        db.add_column('ourmy_app_campaignuser', 'bitly_url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Deleting field 'CampaignUser.api_call'
        db.delete_column('ourmy_app_campaignuser', 'api_call')


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
            'deadline': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '250', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'ourmy_app.campaignuser': {
            'Meta': {'object_name': 'CampaignUser'},
            'api_call': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ourmy_app.Campaign']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_checked': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'ourmy_app.prize': {
            'Meta': {'object_name': 'Prize'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ourmy_app.Campaign']"}),
            'chance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '250', 'blank': 'True'}),
            'dollar_value': ('django.db.models.fields.DecimalField', [], {'default': '10', 'max_digits': '6', 'decimal_places': '2'}),
            'how_many': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'points_value': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'ourmy_app.useraction': {
            'Meta': {'object_name': 'UserAction'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ourmy_app.Action']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'ourmy_app.userprofile': {
            'Meta': {'object_name': 'UserProfile', '_ormbases': ['singly.SinglyProfile']},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'singly_profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'OurmyUserProfile'", 'unique': 'True', 'to': "orm['singly.SinglyProfile']"}),
            'singlyprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['singly.SinglyProfile']", 'unique': 'True', 'primary_key': 'True'})
        },
        'singly.singlyprofile': {
            'Meta': {'object_name': 'SinglyProfile', 'db_table': "'user_profile'"},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profiles': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'singly_id': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['ourmy_app']