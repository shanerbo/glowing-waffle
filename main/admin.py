from django.contrib import admin
from .models import New, NewSeries, NewCategory
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.


class NewAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["new_title", "new_publish"]}),
        ("URL", {"fields": ["new_slug"]}),
        ("Series", {"fields": ["new_series"]}),
        ("Content", {"fields": ["new_content"]}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(New, NewAdmin)
admin.site.register(NewSeries)
admin.site.register(NewCategory)
