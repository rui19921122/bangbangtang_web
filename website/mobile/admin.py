from django.contrib import admin
from main_db.models import *

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass
@admin.register(Customer)
class UserAdmin(admin.ModelAdmin):
    pass
@admin.register(AttentionCourse)
class AttentionAdmin(admin.ModelAdmin):
    pass
