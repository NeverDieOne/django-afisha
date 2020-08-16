from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin
from .models import Place, PlaceImage


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ["place_image", ]
    fields = ('image', 'place_image', 'position')
    extra = 0

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
    raw_id_fields = ["place", ]
