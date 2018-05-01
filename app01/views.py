from django.shortcuts import render, HttpResponse
import json
# Create your views here.


def user(request):
    m = request.GET.get("callback")
    print("请求来了。。。。")
    user_list = [
        "alex", "egon", "eric"
    ]
    v = json.dumps(user_list)
    ret = "%s(%s)" % (m, v)
    return HttpResponse(ret)
