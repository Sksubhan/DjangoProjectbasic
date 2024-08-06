from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'vote.html')


def votede(request):
    if request.method == 'POST':
        a = int(request.POST['age1'])
        if 18 <= a <= 45:
            s = 'Eligible for Elections'
        elif a > 45:
            s = 'NOT Eligible for Elections because age should be below 35'
        else:
            s = "Not Eligible for elections"
        return render(request, "vote.html", {'text': s})
    else:
        return render(request, 'vote.html')
