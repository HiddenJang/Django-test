from django.shortcuts import render
# Create your views here.

def hello(request):
    name = 'John'
    context = {'name': name}
    return render(request, 'hello.html', context)

def childTemplate(request):
    context = {}
    return render(request, 'childTemplate.html', context)
