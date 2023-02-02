from django.shortcuts import render
from .models import MachineData
from django.views.generic import ListView

from django.db.models import Q

def search_page(request):
    return render(
        request,
        'machine_data/search_page.html',
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

# 검색기능 구현 필요
#def index(request):
#    records = MachineData.objects.all()
#    return render(
#        request,
#        'machine_data/search_result.html',
#        {
#            'records':records
#        }
#    )
class MachineList(ListView):
    model = MachineData
    template_name = 'machine_data/search_result.html'

    paginate_by = 5

class MachineSearch(MachineList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        machine_list = MachineData.objects.filter(
            Q(new_l_processsettingname__contains=q) | Q(new_l_machinehistoryname__contains=q)
        ).distinct()
        return machine_list

    def get_context_data(self, **kwargs):
        context = super(MachineSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context




