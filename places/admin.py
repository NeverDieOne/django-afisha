from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin
from .models import Place, PlaceImage


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ["place_image", ]
    fields = ['image', 'place_image', 'position']
    extra = 0

    def place_image(self, obj):
        if obj.id:
            return format_html("<img src={} height={} />", obj.image.url, 200)
        return 'Картинка еще не загружена'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    raw_id_fields = ["place", ]
