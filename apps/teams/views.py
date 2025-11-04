
""" ============ Imports ================ """
from django.shortcuts import render
from apps.teams.models import Team

""" ============= Team Model ================= """
 
def team_list(request):
    """Fetch only active team members, ordered by priority"""
    teams = Team.objects.filter(active=True).order_by('priority')

    context = {
        'teams': teams
    }
    return render(request, 'about_us/team_list.html', context)
