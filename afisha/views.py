from django.shortcuts import render
from places.models import Place


def index(request):
    places = Place.objects.all()
    places_geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in places:
        places_geojson['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": "static/places/moscow_legends.json"
                }
            }
        )

    context = {
        'places': places_geojson
    }
    return render(request, 'index.html', context)
