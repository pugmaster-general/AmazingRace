from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from .models import Clue, Team
from django.views import generic
import django.contrib.auth.decorators
from django.contrib.auth import login, authenticate, update_session_auth_hash
from .forms import VolleyballUpdateForm, JengaUpdateForm


def index(request):
    clues_list = Clue.objects.all()
    context = {'clues_list': clues_list}
    return render(request, 'clues/index.html', context)


def detail(request, clue_id):
    clue = get_object_or_404(Clue, id=clue_id)
    return render(request, 'clues/detail.html', {'clue': clue})


class VolleyballLeaderboard(generic.ListView):
    model = Team
    template_name = 'clues/volleyball.html'
    ordering = ['-volleyball_score']


class JengaLeaderboard(generic.ListView):
    model = Team
    template_name = 'clues/jenga.html'
    ordering = ['-jenga_score']


@django.contrib.auth.decorators.login_required()
def update_volleyball(request):
    if request.method == 'POST':
        form = VolleyballUpdateForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data.get('teams_field')
            team.volleyball_score = form.cleaned_data.get('score')
            team.save()
            message = f"{team}'s volleyball score has been updated to {team.volleyball_score}"

        else:
            message = "error in form"

    else:
        form = VolleyballUpdateForm(initial={'score':0})
        message = ''
    context = {'form':form, 'message':message}

    return render(request, 'clues/update_volleyball.html', context)


@django.contrib.auth.decorators.login_required()
def update_jenga(request):
    if request.method == 'POST':
        form = JengaUpdateForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data.get('teams_field')
            team.jenga_score = form.cleaned_data.get('score')
            team.save()
            message = f"{team}'s jenga score has been updated to {team.jenga_score}"

        else:
            message = "error in form"

    else:
        form = JengaUpdateForm(initial={'score':0})
        message = ''
    context = {'form':form, 'message':message}

    return render(request, 'clues/update_jenga.html', context)
