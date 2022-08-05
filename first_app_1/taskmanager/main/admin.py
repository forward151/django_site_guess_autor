from django.contrib import admin
from .models import TaskF, Table, TableAuthors, Test


admin.site.register(TaskF)
admin.site.register(Table)
admin.site.register(TableAuthors)
admin.site.register(Test)
