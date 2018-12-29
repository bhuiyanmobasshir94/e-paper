from django.contrib import admin

# Register your models here.
from question_model.models import Subject,Paper,Solution,Customer,Chapter,License,Flag

admin.site.register(Subject)
admin.site.register(Paper)
admin.site.register(Solution)
admin.site.register(Customer)
admin.site.register(Chapter)
admin.site.register(License)
admin.site.register(Flag)
