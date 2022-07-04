import site
from django.contrib import admin
from .models import (
    Student,
    Tutor,
    Course,
    MainCategory,
    # Wallet,
    Transaction,
    Visitor,
    PrivateTutor,
    ContractedTutor,
    UnavailableSlot,
    # CourseDetails,
)


# admin.site.register(Student)
# admin.site.register(Tutor)
# admin.site.register(Course)
# admin.site.register(MainCategory)
# admin.site.register(Transaction)
# admin.site.register(Visitor)
# admin.site.register(PrivateTutor)
# admin.site.register(ContractedTutor)
# admin.site.register(UnavailableSlot)
# admin.site.register(CourseDetails)


# # Register your models here.
@admin.register(Student)
class AdminThing(admin.ModelAdmin):
    list_display = [
        "name",
        "age",
        "email",
        "timestamp",
        "updatedtime",
        "_get_courses_student",
    ]
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


@admin.register(Visitor)
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


# @admin.register(CourseDetails)
# class AdminThing(admin.ModelAdmin):
#     list_display = ["course"]
