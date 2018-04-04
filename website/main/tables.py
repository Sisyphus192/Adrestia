import django_tables2 as tables
from .models import Courses

class CourseTable(tables.Table): 
    subject = tables.Column(attrs={"td":{"id":"foo"}})
    class Meta:
        model = Courses
        fields = ("subject", "crse", "crstitle")
        attrs = {'class': 'mytable'}

