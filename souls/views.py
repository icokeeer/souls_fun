from django.shortcuts import render
from django.http import HttpResponse
from .models import SoulsText
from django.views.decorators.csrf import csrf_exempt


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    soul_text = SoulsText.objects.filter(status="validated").order_by('?')[:1]
    # context = {'soul_text': soul_text}
    return render(request, 'index.html', {'soul_text': soul_text})


@csrf_exempt
def boil(request):
    if request.method == 'GET':
        return render(request, 'boil.html')
    elif request.method == 'POST':
        context = request.POST.get('context')
        result = SoulsText.objects.create(
            souls_text=context,
            status='none',
            like_counts=988,
        )
        if result.souls_text == context:
            return render(request, 'boil_response.html')
        else:
            soul_text = '提交失败，请稍后重试...'
            return render(request, 'index.html', {'soul_text': soul_text})



