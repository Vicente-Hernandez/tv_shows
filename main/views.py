from django.shortcuts import render, HttpResponse, redirect
from .models import Networks, Shows
from django.contrib import messages


def index(request):
    return redirect('/shows')


def shows(request):
    shows = Shows.objects.all()
    data = {
        'shows': shows,
    }
    return render(request, 'tv.html', data)


def new(request):
    shows = Shows.objects.all()
    networks = Networks.objects.all()
    data = {
        'shows': shows,
        'networks': networks,
    }
    return render(request, 'new.html', data)


def create(request):
    title = request.POST['title']
    print(title)
    network = int(request.POST['network'])
    print(network)
    date = request.POST['date']
    print(date)
    description = request.POST['description']
    print(description)

    Shows.objects.create(title=title, network_id=network, date=date, description=description)
    messages.success(request, f'The show {title} has been created')
    
    return redirect('/shows')


def info(request, id):
    selected_show = Shows.objects.get(id=id)
    networks = Networks.objects.all()
    shows = Shows.objects.all()
    context = {
        "networks": networks,
        "shows": shows,
        "selected_show": selected_show
    }
    return render(request, 'info.html', context)


def edit(request, id):
    selected_show = Shows.objects.get(id=id)
    networks = Networks.objects.all()
    shows = Shows.objects.all()
    edit_date = selected_show.date.strftime('%Y-%m-%d')

    context = {
        "networks": networks,
        "shows": shows,
        "selected_show": selected_show,
        "edit_date": edit_date,
    }
    return render(request, 'edit.html', context)


def update(request, id):
    selected_show = Shows.objects.get(id=id)
    networks = Networks.objects.all()
    showtitle = request.POST['title']
    networkid = int(request.POST['network'])
    date = request.POST['date']
    description = request.POST['description']

    selected_show.title = showtitle
    selected_show.network_id = networkid
    selected_show.date = date
    selected_show.description = description
    selected_show.save()

    return redirect('/shows/{selected_show.id}/edit')


def destroy(request, id):
    selected_show = Shows.objects.get(id=id)
    temporal = selected_show.title

    context = {
        "temporal": temporal
    }
    messages.error(request, f'Your show {temporal} has been deleted')

    selected_show.delete()
    return redirect("/shows", context)
