from django.contrib import admin

# Register your models here.
from Other_Dao.models import Department, Position


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('ID_department', 'department')

class PositionAdmin(admin.ModelAdmin):
    list_display = ('ID_position', 'ID_department', 'position')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position, PositionAdmin)