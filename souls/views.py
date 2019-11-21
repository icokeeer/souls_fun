from django.shortcuts import render
from django.http import HttpResponse
from .models import SoulsText


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    soul_text = SoulsText.objects.order_by('?')[:1]
    context = {'soul_text': soul_text}
    return render(request, 'index.html', context)
