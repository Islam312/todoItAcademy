from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
  return HttpResponse("hello world!")


def test(request):
  return render(request, 'test.html')

def go(request):
  return render(request, "go.html")


def calc(request):
  f_num = int(input("enter 1st number"))
  s_num = int(input("enter 2nd number"))
  operation_symbol = input("enter operation symbol: ")
  answer = 0
  if operation_symbol == "+":
    answer = f_num + s_num
  elif operation_symbol == "-":
    answer = f_num - s_num
  elif operation_symbol == "*":
    answer = f_num * s_num
  elif operation_symbol == "/":
    answer = f_num / s_num
  return HttpResponse(answer)


def fizz_buzz(request):
  num = int(input("Введите число: "))
  if num % 3 == 0 and num % 5 == 0:
    return HttpResponse("Fizz_Buzz")
  elif num % 3 == 0:
    return HttpResponse("Fizz")
  elif num % 5 == 0:
    return HttpResponse("Buzz")
  else:
    return HttpResponse(num)

