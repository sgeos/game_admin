from django.db import models
from django_extensions.db.models import AutoSlugField

from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class AbstractNamedModel(TimeStampedModel):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class AbstractDynamicFieldModel(AbstractNamedModel):
    default_value = models.IntegerField(_("Default Value"), default=100)
    required = models.BooleanField(_("Required"), default=True)

    class Meta:
        abstract = True


# stats: strength, intelligence, agility, luck, etc.
# skills: sword, axe, polearms, swimming, etc.
class Stat(AbstractDynamicFieldModel):
    class Meta:
        verbose_name = u"stat"
        verbose_name_plural = u"stats"


# physical: slash, bash, pierce, projectile, martial-arts, etc.
# elemental: fire, earth, metal, water, wood, air, dark, light, etc.
# status effects: poison, sleep, mute, blind, petrify, etc.
class EffectType(AbstractDynamicFieldModel):
    class Meta:
        verbose_name = u"effect type"
        verbose_name_plural = u"effect types"


class Unit(AbstractNamedModel):
    stat = models.ManyToManyField(Stat, through='UnitStat')
    defense = models.ManyToManyField(EffectType, through='UnitDefense')

    class Meta:
        verbose_name = u"unit"
        verbose_name_plural = u"units"


class AbstrctValueRelationModel(TimeStampedModel):
    value = models.IntegerField(_("Value"), default=100)
    unit = models.ForeignKey(Unit)
    #relation_type = models.ForeignKey(RelationType)

    #@property
    def owner(self):
        return self.unit.name
    #owner.admin_order_field = 'unit.name'

    class Meta:
        abstract = True
        # unique_together does not work for m2m
        #unique_together = ("unit", "relation_type")


class UnitStat(AbstrctValueRelationModel):
    stat = models.ForeignKey(Stat)

    #@property
    def name(self):
        return self.stat.name
    #name.admin_order_field = 'stat.name'

    class Meta:
        verbose_name = u"unit stat"
        verbose_name_plural = u"unit stats"


class UnitDefense(AbstrctValueRelationModel):
    effect = models.ForeignKey(EffectType)

    #@property
    def name(self):
        return self.effect.name
    #name.admin_order_field = 'effect.name'

    class Meta:
        verbose_name = u"unit defense"
        verbose_name_plural = u"unit defenses"

