from django.contrib import admin

from .models import DoorStatus
# Register your models here.


class DoorStatusAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'status')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        # make all fields readonly
        readonly_fields = list(set(
            [field.name for field in self.opts.local_fields] +
            [field.name for field in self.opts.local_many_to_many]
        ))
        if 'is_submitted' in readonly_fields:
            readonly_fields.remove('is_submitted')
        return readonly_fields


admin.site.register(DoorStatus, DoorStatusAdmin)

