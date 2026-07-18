from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Goal, Alert, Event, Member

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
    confirmed_members = Event.objects.first().confirmed_members.all()

    confirmed_members_list = [member.name for member in confirmed_members]

    print(confirmed_members_list)

    context = {
        'goal': actual_goal,
        'goal_percentage': goal_percentage,
        'goal_message': goal_message,
        'alert_list': alert_list,
        'next_event': next_event,
        'confirmed_members': confirmed_members_list
    }

    return render(request, 'index.html', context)

def confirm_presence(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    number_input = request.POST.get('telefone')
    member = Member.objects.filter(phone_number=number_input).first()

    if not member:
        member_not_found_button = """
        <button disabled
            class="w-full bg-red-500 text-white font-bold py-3 px-4 rounded-lg shadow-md cursor-not-allowed">
            Membro não encontrado!
        </button>
    """

    event.confirmed_members.add(member)

    sucess_button = """
        <button disabled
            class="w-full bg-green-500 text-white font-bold py-3 px-4 rounded-lg shadow-md cursor-not-allowed">
            ✅ Presença Confirmada!
        </button>
    """

    return HttpResponse(sucess_button)
