from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext,loader
from models import BookInfo

# Create your views here.


def index(request):

    booklist = BookInfo.objects.all()
    template = loader.get_template('booktest/index.html')
    context = RequestContext(request,{'booklist':booklist})
    return HttpResponse(template.render(context))
    # return HttpResponse('index')

def detail(request, id):
    book = BookInfo.objects.get(pk=id)
    return render(request, 'booktest/detail.html', {'book': book})