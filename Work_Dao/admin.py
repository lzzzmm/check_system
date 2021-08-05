from django.contrib import admin

# Register your models here.
from Work_Dao.models import Apply, Advise, Task_list, Note

class ApplyAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'apply_day', 'HANDLE_TYPES_CLODR', 'hander', 'process_day')
    list_per_page = 30

class AdviseAdmin(admin.ModelAdmin):
    list_display = ('proposer', 'submit_time', 'HANDLE_TYPES_CLODR', 'hander', 'process_day')
    list_per_page = 30

class Task_list_Admin(admin.ModelAdmin):
    list_display = ('Distributor', 'people_work', 'notice_day', 'closing_day', 'Task_handle_type_CLODR')
    list_per_page = 30


class NoteAdmin(admin.ModelAdmin):
    list_display = ('creator', 'reminder_time', 'modify_time', 'Note_type_CLODR')
    list_per_page = 30

admin.site.register(Apply, ApplyAdmin)
admin.site.register(Advise, AdviseAdmin)
admin.site.register(Task_list, Task_list_Admin)
admin.site.register(Note, NoteAdmin)