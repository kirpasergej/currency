from django.shortcuts import render
from currency.utils import generate_password as gp

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from currency.models import Rate
from currency.models import Source


def generate_password(request):
    password = gp()
    return HttpResponse(password)


def rate_list(request):
    queryset = Rate.objects.all()

    cont = {

        'objects': queryset,
    }

    return render(request, 'rate_list.html', context=cont)


def rate_details(request, pk):
    #    try:
    #       rate = Rate.objects.get(pk=pk)
    #    except Rate.DoesNotExist:
    #        raise Http404(f"Rate does not exist with id{pk}")
    rate = get_object_or_404(Rate, pk=pk)
    cont = {
        'object': rate,
    }
    return render(request, 'rate_details.html', context=cont)


def source_list(request):
    queryset = Source.objects.all()

    cont = {

        'objects': queryset,
    }

    return render(request, 'source_list.html', context=cont)


def source_details(request, pk):
    source = get_object_or_404(Source, pk=pk)
    cont = {
        'object': source,
    }
    return render(request, 'source_details.html', context=cont)
