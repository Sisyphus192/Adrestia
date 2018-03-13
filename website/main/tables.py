import django_tables2 as tables
from .models import Courses

class CourseTable(tables.Table): 
    class Meta:
        model = Courses
        fields = ("crse", "crstitle", "subject")
