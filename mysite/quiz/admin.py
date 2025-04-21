from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text", "explanation"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "explanation"]
    search_fields = ["question_text" "explanation"]

admin.site.register(Question, QuestionAdmin)