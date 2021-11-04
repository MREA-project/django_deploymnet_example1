from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, WebPage, AccessRecord
from first_app import forms


# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    data_dict = {'access_records': webpages_list}
    # return HttpResponse("<em>hello</em>")
    return render(request, 'first_app/index.html', context=data_dict)


def help(request):
    helpdict = {'help_insert': 'HELP PAGE wohoo'}
    return render(request, 'first_app/help.html', context=helpdict)


def home_index(request):
    form = forms.FormName()
    return render(request, 'first_app/homepage.html')


def form_name_views(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Validation success!")
            print("name: " + form.cleaned_data['name'])
            print("email: " + form.cleaned_data['email'])
            print("text: " + form.cleaned_data['text'])
    return render(request, 'first_app/form_page.html', {'form': form})
