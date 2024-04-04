from django.contrib import admin
from .models import Complaints, Forum, User, Marks, Student

admin.site.register(User)
admin.site.register(Forum)
# admin.site.register(Article)
admin.site.register(Student)
admin.site.register(Complaints)

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = ['get_student_name' , 'cgp']

    def get_student_name(self, obj):
        return obj.student.name