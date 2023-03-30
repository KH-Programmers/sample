from django.shortcuts import render, get_object_or_404, redirect
from .models import contentModel
from mainApp import views
import datetime
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
        'text' : content.text,
        'date' : content.date,
        }
    title = 'contents/content'
    return views.main(request, var ,title)

def contentWrite(request):
    title = 'contents/write'
    if request.method == "POST":
        model = contentModel()
        model.date = datetime.datetime.now()
        model.text = request.POST["text"]
        model.Title = request.POST["title"]
        model.save()
        return redirect("conntentApp:index")
    return views.main(request, " ", title)
