from django.shortcuts import render,get_object_or_404
from django.db.models import F
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *
from django.views import generic

app_name="polls"

class IndexView(generic.ListView):
    template_name="polls/index.html"
    context_object_name="questions_list"
    def get_queryset(self):
        return Question.objects.order_by("-publish")[0:5]

class DetailView(generic.DetailView):
    model=Question
    template_name="polls/detail.html"


class ResultsView(generic.DetailView):
    model=Question
    template_name="polls/results.html"


def vote(request,pk):
    question=get_object_or_404(Question,id=pk)
    try:
        selectedChoice=question.choice_set.get(id=request.POST["choice"])
    except(KeyError,Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message":"You did not select a choice"
            },
        )
    else:
        selectedChoice.votes=F("votes")+1
        selectedChoice.save()
        return HttpResponseRedirect(reverse("polls:results",args=(pk,)))
