from django.contrib import admin

from Quickmap.models import QuickMap

class QuickMapAdmin(admin.ModelAdmin):
    search_fields=('subject__subname','subject__level',)
    list_filter=('subject__subname','subject__level')

admin.site.register(QuickMap,QuickMapAdmin)