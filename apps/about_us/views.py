""" ============== Imports ================ """

from django.shortcuts import render

""" ================== Email View =================== """


def our_vision(request):
    return render(request, 'about_us/our_vision.html')

def our_mission(request):
    return render(request, 'about_us/our_mission.html')

def our_team(request):
    return render(request, 'about_us/our_team.html')




