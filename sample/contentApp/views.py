from django.shortcuts import render, get_object_or_404
from .models import contentModel
# Create your views here.
def indexView(request):
    content_list = contentModel.objects.all()
    var = { 'content_list' : content_list}
    return render(request,'contents/index.html',var)

def contentView(request, content_id):
    content = get_object_or_404(contentModel,pk=content_id)
    var = {'Title': content.Title,
           'text' : content.text}
    return render(request,'contents/content.html',var)