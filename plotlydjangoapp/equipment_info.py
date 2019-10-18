from .models import EquipmentInfo2
from django.views.generic import ListView

class equi:
    def get_queryset(self):
        qs = EquipmentInfo2.objects.all()

        return qs
