from django.contrib import admin
from django.forms import TextInput, Textarea, SelectMultiple, DateInput, CheckboxInput, Select
from .models import Students, Instructors, Courses, Major, models
from django.utils.html import format_html


class MajorInline(admin.TabularInline):
    model = Major
    extra = 1

class CourseInline(admin.TabularInline):
    model = Courses
    extra = 1
    

class StudentAdmin(admin.ModelAdmin):
    list_display = ('National_id','Student_id','First_name','Last_name','Birth_date','Units_numbers','is_study_now','created_at','photo_display')
    
    def photo_display(self,obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
    
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('First_name','Last_name','Instructor_degree','is_instructor_now','photo_display')
    list_filter = ("is_instructor_now",)
    search_fields = ('Last_name',)
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 80})}
    }
    
    def photo_display(self,obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('Name_course','Course_credit','Major_id')



admin.site.register(Students,StudentAdmin)
admin.site.register(Instructors, InstructorAdmin)
admin.site.register(Courses,CoursesAdmin)
admin.site.register(Major)