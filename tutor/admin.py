from django.contrib import admin
from .models import Student, Tutor, Course

# Register your models here.
@admin.register(Student)
class AdminThing(admin.ModelAdmin):
    list_display = "__all__"
    list_filter = "__all__"
    search_fields = "__all__"
    # list_per_page = 10
    # list_editable = "__all__"
    # list_display_links = "__all__"
    # list_select_related = "__all__"
    # list_max_show_all = 10
