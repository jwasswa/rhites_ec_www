from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import SourceDocument, OrgUnit, DataElement, DataValue, Category, CategoryCombo, load_excel_to_datavalues

def load_document_values(modeladmin, request, queryset):
    import itertools

    for doc in queryset:
        all_values = load_excel_to_datavalues(doc)
        iter_data_values = itertools.chain.from_iterable(all_values.values())
        DataValue.objects.bulk_create(iter_data_values)

load_document_values.short_description = 'Load data values from document into DB'

class SourceDocumentAdmin(admin.ModelAdmin):
    readonly_fields = ('orig_filename',)
    list_display = ['uploaded_at', 'orig_filename']
    ordering = ['uploaded_at']
    actions = [load_document_values]

class OrgUnitAdmin(MPTTModelAdmin):
    list_display = ['name', 'level']

class DataElementAdmin(admin.ModelAdmin):
    list_display = ['name', 'value_type']

class CategoryComboAdmin(admin.ModelAdmin):
    filter_horizontal = ['categories']
        

class DataValueAdmin(admin.ModelAdmin):
    list_display = ['data_element', 'category_combo', 'site_str', 'org_unit', 'month', 'quarter', 'year', 'numeric_value']
    list_filter = ('data_element__name',)
    search_fields = ['data_element__name', 'category_combo', 'site_str']

admin.site.register(SourceDocument, SourceDocumentAdmin)
admin.site.register(OrgUnit, OrgUnitAdmin)
admin.site.register(DataElement, DataElementAdmin)
admin.site.register(DataValue, DataValueAdmin)
admin.site.register(Category)
admin.site.register(CategoryCombo, CategoryComboAdmin)
