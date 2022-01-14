from django.contrib import admin
from Resources.models import Resource

class ResourceAdmin(admin.ModelAdmin):
    search_fields=('subject__subname','subject__level',)
    list_filter=('subject__subname','subject__level')

admin.site.register(Resource,ResourceAdmin)