from django.shortcuts import render
from currency.utils import generate_password as gp

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from currency.models import Rate
from currency.models import Source
from currency.forms import RateForm
from annoying.functions import get_object_or_None


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


def rate_create(request):
    if request.method == "POST":
        form_data = request.POST
        form = RateForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/rate/list')
    elif request.method == "GET":
        form = RateForm()
    form = RateForm()
    cont = {
        'message': "Rate Create",
        'form': form,
    }
    return render(request, 'rate_create.html', context=cont)


def source_create(request):
    from currency.forms import SourceForm
    form = SourceForm()
    cont = {
        'message': "Source Create",
        'form': form,
    }
    return render(request, 'source_create.html', context=cont)


def rate_update(request, pk):
    instance = get_object_or_404(Rate, pk=pk)

    if request.method == "POST":
        form_data = request.POST
        form = RateForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/rate/list')
    elif request.method == "GET":
        form = RateForm(instance=instance)

    cont = {
        'form': form,
    }
    return render(request, "rate_update.html", context=cont)


def rate_delete(request, pk):
    instance = get_object_or_None(Rate, pk=pk)
    if instance is not None:
        instance.delete()
    return HttpResponseRedirect('/currency/rate/list')
