from django.shortcuts import render
from django.views.generic import TemplateView


class PageMain(TemplateView):
    template_name = 'third_task/main.html'


class Page1(TemplateView):
    template_name = 'third_task/page1.html'


class Page2(TemplateView):
    template_name = 'third_task/page2.html'
