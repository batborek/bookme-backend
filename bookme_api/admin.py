from django.contrib import admin

from bookme_api import models

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_staff',)
    list_filter = ('is_staff',)
    search_fields = ('email',)
    list_per_page = 50

admin.site.register(models.UserProfile, UserAdmin)
admin.site.register(models.Room)
# Register your models here.
