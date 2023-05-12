from django.contrib import admin
from app.models import Author, JobPost, Location, Skills

class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__','title', 'date', 'salary',)
    list_filter = ('date','salary', 'expiry',)
    search_fields = ('title','description', 'salary',)
    search_help_text = "Write in your Query and hit 'Search'  !!!"
    # fields = (('title', 'description'), 'expiry',)
    # exclude = ('title',)
    fieldsets = (
        ('Basic Information', {
         'fields':('title','description')
         }),
         ('More Information', {
         'classes':('collapse','wide',),
         'fields':(('expiry','salary'), 'slug')
         }),
    )

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)