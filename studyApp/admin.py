from django.contrib import admin
from .models import Study, Comment, Tag
# Register your models here.


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'status', 'book', 'location', 'created_at']
    actions = ['make_open',]

    def make_open(self, request, queryset):
        updated_count = queryset.update(status='o')
        self.message_user(request, '{}건의 글을 open 하였습니다.'.format(updated_count))

    def make_close(self, request, queryset):
        updated_count = queryset.update(status='h')
        self.message_user(request, '{}건의 글을 close 하였습니다.'.format(updated_count))

    make_open.short_description = '스터디글 open 상태로 바꾸기'
    make_close.short_description = '스터디글 close 상태로 바꾸기'
#admin.site.register(Study, StudyAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

