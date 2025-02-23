from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

from .models import Organization, Event

# Create your views here.
class HomeView(TemplateView):
    template_name = "cune_connect/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organizations = Organization.objects.all()

        org_data = []
        for org in organizations:
            events = Event.objects.filter(organization=org).exclude(image__isnull=True).exclude(image="")  
            event_images = [event.image.url for event in events]  

            org_data.append({
                "organization": org,
                "event_images": event_images if event_images else ["/static/cune_connect/images/default.jpg"]
            })

        context["latest_organizations"] = org_data
        return context

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
    

def upcoming_events_view(request):
    period = request.GET.get('filter', 'all')
    events = Event.upcoming_events(period=period)
    return render(request, 'cune_connect/upcoming_events.html', {'events': events})




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