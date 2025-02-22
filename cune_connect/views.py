from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Organization, Event

# Create your views here.
class HomeView(generic.ListView):
    template_name = "cune_connect/home.html"
    context_object_name = "latest_organizations"

    def get_queryset(self):
        """Return the organizations."""
        return Organization.objects.order_by("-organization_name")
    

class OrgView(generic.DetailView):
    model = Organization
    template_name = "cune_connect/organization.html"
    

class EventView(generic.DetailView):
    model = Event
    template_name = "cune_connect/event.html"
    context_object_name ="event"

    def get_object(self):
        """Get event based on event_id"""
        event_id = self.kwargs["event_id"]
        return get_object_or_404(Event,pk=event_id)




"""
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        # Redisplay question voting form
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Redirect prevents 2 posts with back button
        return HttpResponseRedirect(reverse("polls:results", args= (question.id,)))

"""