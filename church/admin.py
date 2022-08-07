from urllib.parse import urlencode
from django.contrib import admin
from django.db.models.aggregates import Count
from django.urls import reverse
from django.utils.html import format_html
from . import models

# Register your models here.


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'zone']
    list_select_related = ['zone']
    list_filter = ['zone', 'is_elder', 'is_deacon', 'is_preacher']
    search_fields = ['first_name', 'last_name']
    filter_horizontal = ['ministry']
    autocomplete_fields = ['zone']
    # radio_fields = ['gender', admin.HORIZONTAL]


@admin.register(models.Ministry)
class MinistryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'leader', 'members_count']

    @admin.display(ordering='members_count')
    def members_count(self, ministry):
        url = (
            reverse('admin:church_member_changelist')
            + '?'
            + urlencode({
                'ministry__id': str(ministry.id)
            })
        )
        return format_html('<a href="{}"> {} Members<a/>', url, ministry.members_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(members_count=Count('member'))


@admin.register(models.Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'members_count']
    search_fields = ['title']

    @admin.display(ordering='members_count')
    def members_count(self, zone):
        url = (
            reverse('admin:church_member_changelist')
            + '?'
            + urlencode({
                'zone__id': str(zone.id)
            })
        )
        return format_html('<a href="{}">{} Members</a>', url, zone.members_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            members_count=Count('member')
        )


@admin.register(models.Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'member_id']
    # list_display_links = ['date', 'time']
    list_filter = ['date', 'member_id']
    autocomplete_fields = ['member_id']

    def abscent_member(self, attendance):

        pass
