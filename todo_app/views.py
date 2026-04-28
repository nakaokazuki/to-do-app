from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TodoForm
from .models import Todo


def todo_list(request):
    todos = Todo.objects.order_by("-updated_at")
    titles = [todo.title for todo in todos]
    return HttpResponse("<br>".join(titles) or "To do はまだありません。")


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return HttpResponse(todo.title)


def todo_add(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm()

    return render(request, "todo_app/todo_form.html", {"form": form})


def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_detail", pk=todo.pk)
    else:
        form = TodoForm(instance=todo)

    return render(request, "todo_app/todo_form.html", {"form": form, "todo": todo})


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return HttpResponse(f"{todo.title} の削除画面はこれから作ります。")
