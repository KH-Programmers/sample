from django.shortcuts import render
from django.http import HttpResponse


def main(request, content):
    main = "<h1>main</h1>"
    return HttpResponse(main+content)