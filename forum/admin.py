from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Questions, Answers
import re

class AnswersInline(admin.StackedInline):
    model = Answers
    extra = 1

@admin.register(Questions)

class QuestionsAdmin(ImportExportModelAdmin):
    inlines = [AnswersInline]

    def dehydrate_description(self, Questions):
        return cleanhtml(Questions.description)





def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext