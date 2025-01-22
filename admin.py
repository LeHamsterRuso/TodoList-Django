from django.contrib import admin
from todo_list.models import dyh_task, dyh_project

class ItemAdmin(admin.ModelAdmin):
	list_display = ["name", "priority", "difficulty", "creation_date"]
	searcg_fields = ["name"]

admin.site.register(dyh_task, ItemAdmin)
admin.site.register(dyh_project)
