from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, PlaceImage


class ImageInline(admin.TabularInline):
    model = PlaceImage
    readonly_fields = ["place_image", ]
    fields = ('image', 'place_image', 'position')

    def place_image(self, obj):
        return mark_safe('<img src="{url}" height={height} />'.format(
            url=obj.image.url,
            height=200,
        ))


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    pass
