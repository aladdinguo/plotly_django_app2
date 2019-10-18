from django.contrib import admin
from books.models import Publisher, Author, Book
from plotlydjangoapp.models import EquipmentInfo2, EquipmentOrg


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name']


class BookAdmin(admin.ModelAdmin):
    def show_publisher(self, obj):
        return [i.name for i in obj.publisher.all()]

    def show_Author(self, obj):
        return [[i.last_name, i.first_name] for i in obj.authors.all()]

    list_display = ('title', 'show_publisher', 'show_Author', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    filter_horizontal = ('authors',)


class BookEquipmentInfo2(admin.ModelAdmin):
    list_display = ('name', 'unit_type', 'organization_code', 'organization_name', 'ip')


admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(EquipmentInfo2, BookEquipmentInfo2)
