from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

todos = []

@csrf_exempt
def todo(request):
    if 'todos' not in request.session:
        request.session['todos'] = []
    if request.method == "POST":
        task = request.POST.get("task")
        if task:
            todos.append(task)
            request.session['todos'] = todos
    return render(request, "todo.html", {"todos": request.session['todos']})
