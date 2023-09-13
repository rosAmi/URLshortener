from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Url
import uuid


# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        link_exist = Url.objects.filter(link=link)
        if link_exist:
            obj = get_object_or_404(link_exist, link=link)
            return HttpResponse(obj.uuid)
        else:
            uid = str(uuid.uuid4())[:5]
            new_url = Url(link=link, uuid=uid)
            new_url.save()
            return HttpResponse(uid)


def go(request, pk):
    url_details = get_object_or_404(Url, uuid=pk)
    return redirect(url_details.link)  # 'https://'+
