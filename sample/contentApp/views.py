from django.shortcuts import render, get_object_or_404
from .models import contentModel
from mainApp import views

# Create your views here.
def indexView(request):
    content_list = contentModel.objects.all()
    var = { 'content_list' : content_list }
    title = 'contents/index'
    return views.main(request, var ,title)

def contentView(request, content_id):
    content = get_object_or_404(contentModel,pk=content_id)
    var = {
        'Title': content.Title,
        'text' : content.text
        }
    title = 'contents/content'
    return views.main(request, var ,title)

def contentWrite(request):
    title = 'contents/write'
    return views.main(request, " ", title)
