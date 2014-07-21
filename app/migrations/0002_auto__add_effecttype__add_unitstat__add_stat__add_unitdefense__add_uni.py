# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EffectType'
        db.create_table(u'app_effecttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('default_value', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'app', ['EffectType'])

        # Adding model 'UnitStat'
        db.create_table(u'app_unitstat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=100)),
        ))
        db.send_create_signal(u'app', ['UnitStat'])

        # Adding M2M table for field unit on 'UnitStat'
        m2m_table_name = db.shorten_name(u'app_unitstat_unit')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('unitstat', models.ForeignKey(orm[u'app.unitstat'], null=False)),
            ('unit', models.ForeignKey(orm[u'app.unit'], null=False))
        ))
        db.create_unique(m2m_table_name, ['unitstat_id', 'unit_id'])

        # Adding M2M table for field stat on 'UnitStat'
        m2m_table_name = db.shorten_name(u'app_unitstat_stat')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('unitstat', models.ForeignKey(orm[u'app.unitstat'], null=False)),
            ('stat', models.ForeignKey(orm[u'app.stat'], null=False))
        ))
        db.create_unique(m2m_table_name, ['unitstat_id', 'stat_id'])

        # Adding model 'Stat'
        db.create_table(u'app_stat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('default_value', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'app', ['Stat'])

        # Adding model 'UnitDefense'
        db.create_table(u'app_unitdefense', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=100)),
        ))
        db.send_create_signal(u'app', ['UnitDefense'])

        # Adding M2M table for field unit on 'UnitDefense'
        m2m_table_name = db.shorten_name(u'app_unitdefense_unit')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('unitdefense', models.ForeignKey(orm[u'app.unitdefense'], null=False)),
            ('unit', models.ForeignKey(orm[u'app.unit'], null=False))
        ))
        db.create_unique(m2m_table_name, ['unitdefense_id', 'unit_id'])

        # Adding M2M table for field effect_type on 'UnitDefense'
        m2m_table_name = db.shorten_name(u'app_unitdefense_effect_type')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('unitdefense', models.ForeignKey(orm[u'app.unitdefense'], null=False)),
            ('effecttype', models.ForeignKey(orm[u'app.effecttype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['unitdefense_id', 'effecttype_id'])

        # Adding model 'Unit'
        db.create_table(u'app_unit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'app', ['Unit'])


    def backwards(self, orm):
        # Deleting model 'EffectType'
        db.delete_table(u'app_effecttype')

        # Deleting model 'UnitStat'
        db.delete_table(u'app_unitstat')

        # Removing M2M table for field unit on 'UnitStat'
        db.delete_table(db.shorten_name(u'app_unitstat_unit'))

        # Removing M2M table for field stat on 'UnitStat'
        db.delete_table(db.shorten_name(u'app_unitstat_stat'))

        # Deleting model 'Stat'
        db.delete_table(u'app_stat')

        # Deleting model 'UnitDefense'
        db.delete_table(u'app_unitdefense')

        # Removing M2M table for field unit on 'UnitDefense'
        db.delete_table(db.shorten_name(u'app_unitdefense_unit'))

        # Removing M2M table for field effect_type on 'UnitDefense'
        db.delete_table(db.shorten_name(u'app_unitdefense_effect_type'))

        # Deleting model 'Unit'
        db.delete_table(u'app_unit')


    models = {
        u'app.effecttype': {
            'Meta': {'object_name': 'EffectType'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'default_value': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'app.stat': {
            'Meta': {'object_name': 'Stat'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'default_value': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'app.unit': {
            'Meta': {'object_name': 'Unit'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'app.unitdefense': {
            'Meta': {'object_name': 'UnitDefense'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'effect_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.EffectType']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'unit': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Unit']", 'symmetrical': 'False'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        },
        u'app.unitstat': {
            'Meta': {'object_name': 'UnitStat'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'stat': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Stat']", 'symmetrical': 'False'}),
            'unit': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Unit']", 'symmetrical': 'False'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        }
    }

    complete_apps = ['app']