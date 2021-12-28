# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
import requests, json

from django.shortcuts import render

# Create your views here.

#importando info de PokeAPI
def index(request):
    url= 'https://pokeapi.co/api/v2/pokemon/?limit=10'
    promise = requests.get(url)
    if promise.ok:
        payload=promise.json()
        results=payload.get('results', [])
        listed = []
        if results:
            for pokemon in results:
                pokemonUrl= pokemon['url']
                otherPromise = requests.get(pokemonUrl)
                if otherPromise.ok:
                    payload2= otherPromise.json()
                    pokemon['img']=payload2['sprites']['other']['official-artwork']['front_default']
                    pokemon['id']=payload2['id']
                listed.append(pokemon)

    return render(request, 'pokemon/lista.html', {"list": listed})

def poke_char(request, id_pokemon):
    url_pokemon = 'https://pokeapi.co/api/v2/pokemon/%s' % id_pokemon
    promise = requests.get(url_pokemon)
    if promise.ok:
        results = promise.json()
        pokemon= {}
        pokemon['name'] = results['name']
        pokemon['img']=results['sprites']['other']['official-artwork']['front_default']
        pokemon['weight'] = results['weight']
        pokemon['height'] = results['height']
        pokemon['types'] = results['types']
        for types in pokemon['types']:
            types['type']['url'] = types['type']['url'][31:-1]
        pokemon['abilities'] = results['abilities']
        pokemon['moves'] = results['moves']
    return render(request, 'pokemon/char.html', {'pokemon': pokemon})

def poke_type(request, id_type):
    url='https://pokeapi.co/api/v2/type/%s' % id_type
    promise = requests.get(url)
    if promise.ok:
        payload=promise.json()
        results=payload.get('pokemon', [])
        listed = []
        if results:
            for pokemon in results:
                pokemonUrl= pokemon['pokemon']['url']
                otherPromise = requests.get(pokemonUrl)
                if otherPromise.ok:
                    payload2= otherPromise.json()
                    pokemon['img']=payload2['sprites']['other']['official-artwork']['front_default']
                    pokemon['id']=payload2['id']
                pokemon['name'] = pokemon['pokemon']['name']
                listed.append(pokemon)
                
    return render(request, 'pokemon/lista.html', {"list": listed})
