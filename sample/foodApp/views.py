from django.shortcuts import render
from django.http import HttpResponse
from mainApp import views
from datetime import datetime
import json
import requests

# Create your views here.
def load(request) :
    content = foodGet()
    title = "food/food"
    return views.main(request, content, title)

def foodGet() :
    date = datetime.today().strftime("%Y%m%d") 
    url = "https://open.neis.go.kr/hub/mealServiceDietInfo?key=16c6ed183ccf402dbff0d174ff8a04d7&Type=jsonp&Index=1&pSize=100&ATPT_OFCDC_SC_CODE=B10&SD_SCHUL_CODE=7010126&MLSV_YMD="+date
    response = requests.get(url)
    contents = response.text
    print(contents)
    json_ob = json.loads(contents)
    if list(json_ob.keys())[0] == "RESULT":
        body = "오늘 급식이 없습니다."
    else:
        body = json_ob['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
    return body

