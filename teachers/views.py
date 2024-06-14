from django.shortcuts import render

def roster(request):
    context = {
        'first_name': 'Margaret',
        'last_name': 'Bulishko',
        'phone': '067554212',
        'age': '22',
        'experience': '3',
        'specialization': 'English, Polish, Ukrainian language teacher'
    }
    return render(request, "teachers/roster_mentors.html", context)

def mentors(request):
    context = {
        'first_name': 'Margaret',
        'last_name': 'Bulishko',
        'phone': '067554212',
        'age': '22',
        'experience': '3',
        'specialization': 'English, Polish, Ukrainian language teacher'
    }
    return render(request, "teachers/card_mentor.html", context)