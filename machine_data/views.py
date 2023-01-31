from django.shortcuts import render
from .models import MachineData

def index(request):
    records = MachineData.objects.all()
    return render(
        request,
        'machine_data/result.html',
        {
            'records':records
        }
    )

def machine_detail_page(request, pk):
    record = MachineData.objects.get(pk=pk)

    return render(
        request,
        'machine_data/machine_detail_page.html',
        {
            'record':record,
        }
    )