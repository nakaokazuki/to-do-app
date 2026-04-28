from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    scheduled_at = forms.DateTimeField(
        required=False,
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"},
            format="%Y-%m-%dT%H:%M",
        ),
        label="日時",
    )

    class Meta:
        model = Todo
        fields = [
            "title",
            "scheduled_at",
            "location",
            "caution",
            "preparation",
            "detail",
        ]
        labels = {
            "title": "To do",
            "location": "場所",
            "caution": "注意事項",
            "preparation": "準備が必要なもの",
            "detail": "より詳しい内容",
        }
        widgets = {
            "caution": forms.Textarea(attrs={"rows": 3}),
            "preparation": forms.Textarea(attrs={"rows": 3}),
            "detail": forms.Textarea(attrs={"rows": 5}),
        }
