from django.contrib import admin

from app.models import JobPost

class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__','title', 'date', 'salary',)
    list_filter = ('date','salary', 'expiry',)
    search_fields = ('title','description', 'salary',)
    search_help_text = "Write in your Query and hit 'Search'!!!"


# Register your models here.
admin.site.register(JobPost, JobAdmin)