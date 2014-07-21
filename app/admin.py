from django.contrib import admin
from .models import Unit, Stat, EffectType, \
                    UnitStat, UnitDefense
import reversion


class UnitStatInline(admin.TabularInline):
    model = UnitStat
    extra = 3

class UnitDefenseInline(admin.TabularInline):
    model = UnitDefense
    extra = 3

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
    inlines = (UnitStatInline,)

class EffectTypeAdmin(reversion.VersionAdmin):
    fieldsets = (
        (None, {
            'fields': (('name', 'default_value', 'required'),)
        }),
    )
    list_display = ('id', 'name', 'default_value', 'required', 'created', 'modified')
    inlines = (UnitDefenseInline,)

class UnitStatAdmin(reversion.VersionAdmin):
    list_display = ('id', 'owner', 'name', 'value')

class UnitDefenseAdmin(reversion.VersionAdmin):
    list_display = ('id', 'owner', 'name', 'value')

admin.site.register(Stat, StatAdmin)
admin.site.register(EffectType, EffectTypeAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(UnitStat, UnitStatAdmin)
admin.site.register(UnitDefense, UnitDefenseAdmin)

