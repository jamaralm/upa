from django.shortcuts import render
from django.http import HttpResponse

from .models import Goal, Alert, Event

def index(request):

    '''
    GOALS
    '''
    actual_goal = Goal.objects.first()
    goal_message = actual_goal.__str__()

    if not actual_goal:
        goal_message = "Sem Meta no Momento!"

    goal_percentage = int((actual_goal.value_collected / actual_goal.value) * 100)

    '''
    ALERTS
    '''
    alert_list = Alert.objects.all().order_by('-datetime')[:2]

    '''
    EVENT
    '''
    next_event = Event.objects.order_by('-event_date').first()

    context = {
        'goal': actual_goal,
        'goal_percentage': goal_percentage,
        'goal_message': goal_message,
        'alert_list': alert_list,
        'next_event': next_event
    }

    return render(request, 'index.html', context)