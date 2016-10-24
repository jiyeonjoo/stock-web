import json

from django.http.response import HttpResponse
from django.shortcuts import render_to_response


def index(request):
    stock_data = dict(
        company="삼성전자",
        code="005930",
        price=10000,
        high=11000,
        low=9000,
        volume=1000,
    )
    stock_data2 = dict(stock_data)
    stock_data2["company"] = "삼성전기"
    stock_data2["price"] = 11000
    stock_data2["code"] = "005940"

    context = dict(
        stock_data_list = [stock_data, stock_data2]
    )

    return render_to_response('index.html', context)


def company_info(request, code):
    # database

    company_info = dict()
    print(code)

    return render_to_response('company_info.html', company_info)