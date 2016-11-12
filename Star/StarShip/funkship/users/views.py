from django.shortcuts import get_object_or_404, render
#from django.template import loader
from django.http import HttpResponse

from .models import User
from .models import Room

# Create your views here.
def index(request):
    return HttpResponse("Welcome %s" % "GhostShell")

def users(request):
    registered_users = User.objects.all()
    #template = loader.get_template('users/index.html')
    context = {
        'registered_users': registered_users,
    }

    #return HttpResponse("Current users in database %s" % registered_users)
    return render(request, 'users/index.html', context)

def browser(request):
    current_rooms = Room.objects.all()
    context = {
        'current_rooms': current_rooms,
    }

    #return HttpResponse("Current users in database %s" % registered_users)
    return render(request, 'users/browser.html', context)

def detail(request):
    #question = get_object_or_404(User, pk=user_id)
    return render(request, 'users/detail.html', {'status': ['online', 'offline']})

