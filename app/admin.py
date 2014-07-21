from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from .models import Unit, Stat, EffectType, \
                    UnitStat, UnitDefense
import reversion


class UnitStatInlineFormSet(BaseInlineFormSet):
    model = UnitStat

    def __init__(self, *args, **kwargs):
        super(UnitStatInlineFormSet, self).__init__(*args, **kwargs)
        obj = kwargs['instance']
        all_required = Stat.objects.filter(required=True)
        obj_existing = UnitStat.objects.filter(unit=obj.id)
        obj_required = obj_existing.filter(stat__required=True)
        obj_optional = obj_existing.filter(stat__required=False)
        result = []
        ### This puts everything in order, but deleting is broken
        # for stat in all_required:
        #     if 0 < obj_existing.filter(stat__name=stat.name).count():
        #         value = obj_existing.filter(stat__name=key)[0].value
        #         result.append({'stat': stat.id, 'value': value})
        #     else:
        #         result.append({'stat': stat.id, 'value': stat.default_value})
        # for stat in obj_optional:
        #     result.append({'stat': stat.stat.id, 'value': stat.value})
        for stat in obj_required:
            result.append({'stat': stat.stat.id, 'value': stat.value})
        for stat in obj_optional:
            result.append({'stat': stat.stat.id, 'value': stat.value})
        for stat in all_required:
            if 0 < obj_existing.filter(stat__name=stat.name).count():
                pass
            else:
                ### Default value is not working...
                result.append({'stat': stat.id, 'value': stat.default_value})
                # result.append({'stat': stat.id, 'value': ''})
        self.initial = result


class UnitStatInline(admin.TabularInline):
    fieldsets = (
        (None, {
            'fields': (('unit', 'stat', 'value'),)
        }),
    )
    # readonly_fields = ['unit', 'stat']
    model = UnitStat
    formset = UnitStatInlineFormSet

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(UnitStatInline, self).get_formset(request, obj, **kwargs)
        formset.request = request
        return formset

    def get_extra(self, request, obj=None, **kwargs):
        # extra = super(UnitStatInline, self).get_extra(request, obj, **kwargs)
        result = Stat.objects.filter(required=True).count()
        if obj:
            result -= UnitStat.objects.filter(unit=obj.id).filter(stat__required=True).count() 
        #something = request.GET.get('something', None)
        #if something:
        #    extra = 1#... figure out how much initial forms there are, from the request ...
        return result


class UnitDefenseInlineFormSet(BaseInlineFormSet):
    model = UnitDefense

    def __init__(self, *args, **kwargs):
        super(UnitDefenseInlineFormSet, self).__init__(*args, **kwargs)
        obj = kwargs['instance']
        all_required = EffectType.objects.filter(required=True)
        obj_existing = UnitDefense.objects.filter(unit=obj.id)
        obj_required = obj_existing.filter(effect__required=True)
        obj_optional = obj_existing.filter(effect__required=False)
        result = []
        ### This puts everything in order, but deleting is broken
        # for effect in all_required:
        #     if 0 < obj_existing.filter(effect__name=effect.name).count():
        #         value = obj_existing.filter(effect__name=key)[0].value
        #         result.append({'effect': effect.id, 'value': value})
        #     else:
        #         result.append({'effect': effect.id, 'value': effect.default_value})
        # for effect in obj_optional:
        #     result.append({'effect': effect.effect.id, 'value': effect.value})
        for effect in obj_required:
            result.append({'effect': effect.effect.id, 'value': effect.value})
        for effect in obj_optional:
            result.append({'effect': effect.effect.id, 'value': effect.value})
        for effect in all_required:
            if 0 < obj_existing.filter(effect__name=effect.name).count():
                pass
            else:
                ### Default value is not working...
                result.append({'effect': effect.id, 'value': effect.default_value})
                # result.append({'effect': effect.id, 'value': ''})
        self.initial = result


class UnitDefenseInline(admin.TabularInline):
    fieldsets = (
        (None, {
            'fields': (('unit', 'effect', 'value'),)
        }),
    )
    # readonly_fields = ['unit', 'effect']
    model = UnitDefense
    formset = UnitDefenseInlineFormSet

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(UnitDefenseInline, self).get_formset(request, obj, **kwargs)
        formset.request = request
        return formset

    def get_extra(self, request, obj=None, **kwargs):
        # extra = super(UnitDefenseInline, self).get_extra(request, obj, **kwargs)
        result = EffectType.objects.filter(required=True).count()
        if obj:
            result -= UnitDefense.objects.filter(unit=obj.id).filter(effect__required=True).count()
        #something = request.GET.get('something', None)
        #if something:
        #    extra = 1#... figure out how much initial forms there are, from the request ...
        return result


class UnitAdmin(reversion.VersionAdmin):
    list_display = ('id', 'name', 'created', 'modified')
    inlines = (UnitStatInline, UnitDefenseInline)

class StatAdmin(reversion.VersionAdmin):
    fieldsets = (
        (None, {
            'fields': (('name', 'default_value', 'required'),)
        }),
    )
    list_display = ('id', 'name', 'default_value', 'required', 'created', 'modified')
    # inlines = (UnitStatInline,)

class EffectTypeAdmin(reversion.VersionAdmin):
    fieldsets = (
        (None, {
            'fields': (('name', 'default_value', 'required'),)
        }),
    )
    list_display = ('id', 'name', 'default_value', 'required', 'created', 'modified')
    # inlines = (UnitDefenseInline,)

# class UnitStatAdmin(reversion.VersionAdmin):
#     fieldsets = (
#         (None, {
#             'fields': (('unit', 'stat', 'value'),)
#         }),
#     )
#     list_display = ('id', 'owner', 'name', 'value')

# class UnitDefenseAdmin(reversion.VersionAdmin):
#     fieldsets = (
#         (None, {
#             'fields': (('unit', 'effect', 'value'),)
#         }),
#     )
#     list_display = ('id', 'owner', 'name', 'value')

admin.site.register(Unit, UnitAdmin)
admin.site.register(Stat, StatAdmin)
admin.site.register(EffectType, EffectTypeAdmin)
# admin.site.register(UnitStat, UnitStatAdmin)
# admin.site.register(UnitDefense, UnitDefenseAdmin)

# TODO: 
#   Prevent duplicate entries on unit save.
#   Save default values on unit save.

