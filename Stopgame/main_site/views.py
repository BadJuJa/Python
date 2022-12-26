from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import BSParser.parse


@csrf_exempt
def about(request):
    args = {
        'title': 'About',
        'h_class': '',
        'a_class': 'active',
        'c_class': '',
    }
    return render(request, 'about.html', args)


def contacts(request):
    args = {
        'title': 'Contacts',
        'h_class': '',
        'a_class': '',
        'c_class': 'active',
    }
    return render(request, 'contacts.html', args)


@csrf_exempt
def search_result(request):
    if request.method == 'POST':
        fy = int(request.POST.get('from_year_input'))
        ty = int(request.POST.get('to_year_input'))
        c = int(request.POST.get('count_input'))
        games = BSParser.parse.parse(fy, ty)
        if c == -1:
            c = len(games.keys())
        show = list(games.keys())[:c]
        games_dict = {}
        for game in show:
            games_dict[game] = {
                'name': game,
                'link': games[game]['link'],
                'picture_link': games[game]['picture_link'],
                'rating': games[game]['rating']
            }
        args = {
            'title': 'Results',
            'h_class': 'active',
            'a_class': '',
            'c_class': '',
            'games_dict': games_dict
        }
        return render(request, 'index.html', args)
    else:
        context = {}
        return render(request, 'index.html', context)


@csrf_exempt
def search_view(request, *args, **kwargs):
    args = {
        'title': 'Home',
        'h_class': 'active',
        'a_class': '',
        'c_class': '',
    }
    return render(request, 'index.html', args)
