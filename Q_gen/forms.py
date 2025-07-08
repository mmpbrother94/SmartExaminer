# generator/forms.py
from django import forms
from .models import UploadedText

class UploadedTextForm(forms.ModelForm):
    class Meta:
        model = UploadedText
        fields = ['title', 'file', 'class_name', 'subject', 'exam_name', 'total_questions', 'duration', 'full_marks']
