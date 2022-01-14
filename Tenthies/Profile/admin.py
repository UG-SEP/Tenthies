from django.contrib import admin

from Profile.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    search_fields=('user__username','chname','level','best_subject','weak_subject')
    list_filter=('chname','level','best_subject','weak_subject')

admin.site.register(Profile,ProfileAdmin)