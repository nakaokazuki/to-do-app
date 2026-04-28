from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Todo


def todo_list(request):
    todos = Todo.objects.order_by("-updated_at")
    titles = [todo.title for todo in todos]
    return HttpResponse("<br>".join(titles) or "To do はまだありません。")


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return HttpResponse(todo.title)


def todo_add(request):
    return HttpResponse("To do 追加画面はこれから作ります。")


def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return HttpResponse(f"{todo.title} の編集画面はこれから作ります。")


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return HttpResponse(f"{todo.title} の削除画面はこれから作ります。")
