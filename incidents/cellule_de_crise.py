from django.shortcuts import render , redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import Profile , CelluleDeCrise
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Event
import socket

def envoi_mail(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.role == 'adminapp':   
        if request.method == 'POST':
            name = request.POST.get('name')
            emails = request.POST.get('email')  # Accept multiple emails separated by commas
            message = request.POST.get('message')

            # Split emails by commas and strip any whitespace
            email_list = [email.strip() for email in emails.split(',')]

            try:
                send_mail(
                    name,
                    message,
                    'settings.EMAIL_HOST_USER',
                    email_list,  # Pass the list of emails here
                    fail_silently=False
                )
                return redirect('cellule_de_crise')
            except (socket.gaierror, socket.timeout, ConnectionError):
                return render(request, 'internet_connection.html')
        else:
            agenda = CelluleDeCrise.objects.all()
            context = {'profile': profile}
            return render(request, 'cellule/mail.html', context)
    else: 
        return render(request, 'permission.html')


import logging

logger = logging.getLogger(__name__)

@csrf_exempt
@csrf_exempt
def add_event(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.role == 'adminapp':
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                day = data['day']
                month = data['month']
                year = data['year']
                event = data['event']

                # Load the Event object and manually check if the event already exists
                event_obj, created = Event.objects.get_or_create(day=day, month=month, year=year)
                if event_obj.events is None:
                    event_obj.events = []

                # Check if the event already exists in the events list
                if event in event_obj.events:
                    return JsonResponse({'success': False, 'message': 'Event already added'})

                event_obj.events.append(event)
                event_obj.save()

                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)})

        return JsonResponse({'success': False, 'message': 'Invalid request method'})
    else:
        return render(request, 'permission.html')


@csrf_exempt
def delete_event(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.role == 'adminapp' or profile.role:
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                day = data['day']
                month = data['month']
                year = data['year']
                event_title = data['event_title']

                event_obj = Event.objects.get(day=day, month=month, year=year)
                events = event_obj.events
                
                # Find the event to delete
                for idx, event in enumerate(events):
                    if event['title'] == event_title:
                        events.pop(idx)
                        break

                # If no events left in a day, delete the entire event object
                if not events:
                    event_obj.delete()
                else:
                    # Save the updated events list
                    event_obj.events = events
                    event_obj.save()

                return JsonResponse({'success': True, 'message': 'Event deleted successfully'})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)})

        return JsonResponse({'success': False, 'message': 'Invalid request method'})

def cellule_view(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.role == 'adminapp' or profile.role == 'superviseur':  
        eventquery = Event.objects.all()
        events = list(eventquery.values('day', 'month', 'year', 'events'))
        context = {'events': json.dumps(events) , 'profile':profile}
        return render(request, 'cellule/cellule.html', context)
    else: 
        return render(request , 'permission.html')
