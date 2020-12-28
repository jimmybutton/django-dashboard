from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from .models import City

def home(request):
    return render(request, 'home.html')

def population_chart(request):
    labels = []
    data = []

    queryset = City.objects.values('country__name') \
        .annotate(country_population=Sum('population')) \
        .order_by('-country_population')
    
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def city_chart(request):
    labels = []
    data = []

    limit = int(request.GET.get('limit', 20))

    queryset = City.objects \
        .order_by('-population')[:limit]
    
    for entry in queryset:
        labels.append(entry.name)
        data.append(entry.population)
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
