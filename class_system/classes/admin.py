from django.contrib import admin
from .models import Classes, Enrollments
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta, date

class ClassesAdmin(admin.ModelAdmin):
    list_display = ('title_age_group', 'start_date', 'day_of_week', 'time_slot', 'is_active')
    actions = ['make_active', 'make_inactive']

    def title_age_group(self, obj):
        return f'{obj.title} (Age {obj.age_group})'
    title_age_group.short_description = 'Title'

    @admin.action(description="Make Active")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Make Inactive")
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)


admin.site.register(Classes, ClassesAdmin)
admin.site.register(Enrollments)