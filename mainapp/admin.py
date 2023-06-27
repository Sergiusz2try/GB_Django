from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from mainapp import models as mainapp_models


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "deleted"]
    search_fields = ["title", "preamble", "body"]
    actions = ["mark_deleted"]

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")


@admin.register(mainapp_models.Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'num', 'title', 'created']
    ordering = ['-id']
    list_per_page = 5
    list_filter = ["course", "created"]

    # def get_course_name(self, obj):
    #     return obj.course.name
    #
    # get_course_name.short_description = _("Course")
