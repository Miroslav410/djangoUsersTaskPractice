from django.shortcuts import render

# from personal.models import Question

from account.models import Account

# Create your views here.

def home_screen_view(request):
    # print(request.headers)

    context = {}
    # context['some_string'] = "This is some string that I'm passing to the view"
    # context['some_number'] = 12321421

    # context = {
    #
    #     'some_string' : "This is some string that I'm passing to the view",
    #     'some_number' : 312312135,
    #
    # }

    # list_of_values = []
    # list_of_values.append('first entry')
    # list_of_values.append('second entry')
    # list_of_values.append('third entry')
    # list_of_values.append('fourth entry')
    # context['list_of_values'] = list_of_values

    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, 'personal/home.html', context)