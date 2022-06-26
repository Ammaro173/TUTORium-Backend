from django.contrib import admin
from .models import (
    Student,
    Tutor,
    Course,
    MainCategory,
    University,
    # Wallet,
    Transaction,
    User,
    PrivateTutor,
    ContractedTutor,
    UnavailableSlot,
)

# Register your models here.
@admin.register(Student)
class AdminThing(admin.ModelAdmin):
    list_display = ["name", "age", "email", "timestamp", "updatedtime"]
    # list_filter = "__all__"
    # search_fields = "__all__"
    # list_per_page = 10
    # list_editable = "__all__"
    # list_display_links = "__all__"
    # list_select_related = "__all__"
    # list_max_show_all = 10


@admin.register(Course)
class AdminThing(admin.ModelAdmin):
    list_display = ["name", "course_category"]


@admin.register(MainCategory)
class AdminThing(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Tutor)
class AdminThing(admin.ModelAdmin):
    list_display = ["name", "age", "teaching_experience", "category", "_get_courses"]


@admin.register(Transaction)
class AdminThing(admin.ModelAdmin):
    list_display = ["user", "amount", "date", "time"]


@admin.register(User)
class AdminThing(admin.ModelAdmin):
    list_display = ["name", "email", "password"]


@admin.register(PrivateTutor)
class AdminThing(admin.ModelAdmin):
    list_display = ["name", "age", "teaching_experience", "category", "rate"]


@admin.register(ContractedTutor)
class AdminThing(admin.ModelAdmin):
    list_display = ["name", "age", "teaching_experience", "category"]


@admin.register(UnavailableSlot)
class AdminThing(admin.ModelAdmin):
    list_display = ["tutor", "date", "time_start", "duration"]
