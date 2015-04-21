from django.shortcuts import render_to_response

from .forms import NotesSearchForm
from haystack.utils.geo import Point


def notes(request):
    form = NotesSearchForm(request.GET)
    notes = form.search()
    return render_to_response('notes.html', {'notes': notes})