from django.conf.urls import url
from views import index, poke_char, poke_type



urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^char/(?P<id_pokemon>\d+)$', poke_char, name="pokemon_char"),
    url(r'^type/(?P<id_type>\d+)$', poke_type, name='pokemon_type')
]