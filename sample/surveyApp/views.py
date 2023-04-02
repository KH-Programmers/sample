from django.shortcuts import render
from django.http import HttpResponse
from mainApp import views
import slack_sdk

stoken = 'xoxb-5060008758977-5047395059074-uxWRo9uD2Zdw622O5MpVZqcn'
schannel = 'C051ACXGBQD'

def load(request):
    title = "survey/survey"
    name = request.POST.get('name')
    number = request.POST.get('number')
    report_type = request.POST.get('report_type')
    msg = request.POST.get('msg')
    
    if (number is not None):
        client = slack_sdk.WebClient(token=stoken)
        client.chat_postMessage(channel=schannel, text=f"이름: {name}\n학번: {number}\n건의 종류: {report_type}\n건의내용: {msg}")

    else:
        pass
    
    content = ""
    return views.main(request, content, title)