from django.shortcuts import render, HttpResponse
from .models import ToDo
# Create your views here.
def homepage(request):
  todo_list = ToDo.objects.all()
  return render(request,'index.html', {'todo_list': todo_list})

def test(request):
  todo_list = ToDo.objects.all()
  return render(request, 'test.html',{'todo_list': todo_list})

