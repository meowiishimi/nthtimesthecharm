from django.shortcuts import render, redirect
from .models import Agent
from .forms import AgentForm

def agent_list(request):
    agent = Agent.objects.select_related('building').prefetch_related('venues')
    return render(request, 'agent/agent_list.html', {'agents': agent})

def add_agent(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agent_list')
    else:
        form = AgentForm()
    return render(request, 'agent/agent_form.html', {'form': form})
