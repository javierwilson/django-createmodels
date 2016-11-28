from django.contrib import admin
from createmodels.models import Model, Field

class FieldInline(admin.TabularInline):
    model = Field
    fk_name = 'model'
    extra = 1

class ModelAdmin(admin.ModelAdmin):
    inlines = [
        FieldInline,
    ]


admin.site.register(Model, ModelAdmin)

admin.site.register(Field)
