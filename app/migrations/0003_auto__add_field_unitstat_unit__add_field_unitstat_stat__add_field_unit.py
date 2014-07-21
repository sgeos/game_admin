# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UnitStat.unit'
        db.add_column(u'app_unitstat', 'unit',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['app.Unit']),
                      keep_default=False)

        # Adding field 'UnitStat.stat'
        db.add_column(u'app_unitstat', 'stat',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['app.Stat']),
                      keep_default=False)

        # Removing M2M table for field stat on 'UnitStat'
        db.delete_table(db.shorten_name(u'app_unitstat_stat'))

        # Removing M2M table for field unit on 'UnitStat'
        db.delete_table(db.shorten_name(u'app_unitstat_unit'))

        # Adding field 'UnitDefense.unit'
        db.add_column(u'app_unitdefense', 'unit',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['app.Unit']),
                      keep_default=False)

        # Adding field 'UnitDefense.effect'
        db.add_column(u'app_unitdefense', 'effect',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['app.EffectType']),
                      keep_default=False)

        # Removing M2M table for field effect_type on 'UnitDefense'
        db.delete_table(db.shorten_name(u'app_unitdefense_effect_type'))

        # Removing M2M table for field unit on 'UnitDefense'
        db.delete_table(db.shorten_name(u'app_unitdefense_unit'))


    def backwards(self, orm):
        # Deleting field 'UnitStat.unit'
        db.delete_column(u'app_unitstat', 'unit_id')

        # Deleting field 'UnitStat.stat'
        db.delete_column(u'app_unitstat', 'stat_id')

        # Adding M2M table for field stat on 'UnitStat'
        m2m_table_name = db.shorten_name(u'app_unitstat_stat')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('unitstat', models.ForeignKey(orm[u'app.unitstat'], null=False)),
            ('stat', models.ForeignKey(orm[u'app.stat'], null=False))
        ))
        db.create_unique(m2m_table_name, ['unitstat_id', 'stat_id'])

        # Adding M2M table for field unit on 'UnitStat'
        m2m_table_name = db.shorten_name(u'app_unitstat_unit')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('unitstat', models.ForeignKey(orm[u'app.unitstat'], null=False)),
            ('unit', models.ForeignKey(orm[u'app.unit'], null=False))
        ))
        db.create_unique(m2m_table_name, ['unitstat_id', 'unit_id'])

        # Deleting field 'UnitDefense.unit'
        db.delete_column(u'app_unitdefense', 'unit_id')

        # Deleting field 'UnitDefense.effect'
        db.delete_column(u'app_unitdefense', 'effect_id')

        # Adding M2M table for field effect_type on 'UnitDefense'
        m2m_table_name = db.shorten_name(u'app_unitdefense_effect_type')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('unitdefense', models.ForeignKey(orm[u'app.unitdefense'], null=False)),
            ('effecttype', models.ForeignKey(orm[u'app.effecttype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['unitdefense_id', 'effecttype_id'])

        # Adding M2M table for field unit on 'UnitDefense'
        m2m_table_name = db.shorten_name(u'app_unitdefense_unit')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('unitdefense', models.ForeignKey(orm[u'app.unitdefense'], null=False)),
            ('unit', models.ForeignKey(orm[u'app.unit'], null=False))
        ))
        db.create_unique(m2m_table_name, ['unitdefense_id', 'unit_id'])


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
            'defense': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.EffectType']", 'through': u"orm['app.UnitDefense']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'stat': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Stat']", 'through': u"orm['app.UnitStat']", 'symmetrical': 'False'})
        },
        u'app.unitdefense': {
            'Meta': {'object_name': 'UnitDefense'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.EffectType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Unit']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        },
        u'app.unitstat': {
            'Meta': {'object_name': 'UnitStat'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'stat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Stat']"}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Unit']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        }
    }

    complete_apps = ['app']