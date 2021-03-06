from django.core.management.base import BaseCommand
import requests
from places.models import Place, PlaceImage
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Add place to map by json object'

    def add_arguments(self, parser):
        parser.add_argument('url', help='URL to download json file with place')

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        response.raise_for_status()

        place_json = response.json()
        title = place_json['title']
        imgs = place_json['imgs']
        desc_short = place_json['description_short']
        desc_long = place_json['description_long']
        lng, lat = place_json['coordinates'].values()

        place, _ = Place.objects.get_or_create(
            title=title,
            short_description=desc_short,
            long_description=desc_long,
            lat=lat,
            lng=lng
        )

        for index, img in enumerate(imgs):
            response = requests.get(img)
            response.raise_for_status()

            image_content = ContentFile(response.content)
            place_image_obj = PlaceImage.objects.create(
                place=place,
                position=index
            )

            place_image_obj.image.save(f'{place.pk}-{index}.jpg', image_content, save=True)
