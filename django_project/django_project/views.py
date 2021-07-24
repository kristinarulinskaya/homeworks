from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class BadRequestView(View):
    def get(self, request):
        return HttpResponse(status=400)


class SuccessRequestView(View):
    def get(self, request):
        return HttpResponse(status=200)

