from django.shortcuts import render
from django.http import HttpResponse

def main(request, content, title):
    cont = {
        'title' : title,
        'content' : content
    }

    return render(request,  title+".html", cont)