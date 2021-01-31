from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Books
# Create your views here.
def homepage(request):
  todo_list = ToDo.objects.all()
  return render(request,'index.html', {'todo_list': todo_list})

def test(request):
  todo_list = ToDo.objects.all()
  return render(request, 'test.html',{'todo_list': todo_list})

def books(request):
  books_list = Books.objects.all()
  return render(request, 'books.html', {'books_list': books_list})

def add_task(request):
  getForm = request.POST
  text = getForm["create_task"]
  todoList = ToDo(describe_text = text)
  todoList.save()
  return redirect(homepage)