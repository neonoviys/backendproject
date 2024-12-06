# views.py
from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse("Hello World!")


def person_info(request, name, age):
    return render(request, 'person_info.html', {'name': name, 'age': age})


def post_example(request):
    post_data = None
    if request.method == 'POST':
        post_data = request.POST.get('data_input')
    return render(request, 'index.html', {'post_data': post_data})
