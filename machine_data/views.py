from django.shortcuts import render
from .models import MachineData

def search_page(request):
    return render(
        request,
        'machine_data/search_page.html',
    )

# 검색기능 구현 필요
def index(request):
    records = MachineData.objects.all()
    return render(
        request,
        'machine_data/search_result.html',
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