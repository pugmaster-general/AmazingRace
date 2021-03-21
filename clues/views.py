from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from .models import Clue


def index(request):
    clues_list = Clue.objects.all()
    context = {'clues_list': clues_list}
    return render(request, 'clues/index.html', context)


def detail(request, clue_id):
    clue = get_object_or_404(Clue, id=clue_id)
    return  render(request, 'clues/detail.html', {'clue': clue})

