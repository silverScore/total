# from django.http import Http404
# from django.shortcuts import render, get_object_or_404
# from django.core.exceptions import BadRequest
from django.views.generic import ListView, DetailView
from .models import Care, Address
# from .models import Review
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

# listview
class CareListView(ListView):
    model = Care
    template_name = 'care_list.html'
    paginate_by = 10  # 페이지당 10개씩 보여주기


    def get_context_data(self, **kwargs):
        context = super(CareListView, self).get_context_data(**kwargs)
        context['care_list'] = Care.objects.order_by('ratingGrade','-ratingCd')
        context['address_info'] = Address.objects.all()
        context['siDo_info'] = Address.objects.filter(siGunGuCd__gt=0, DongCd__gt=0).order_by('siDoCd','siGunGuCd','DongCd').values()

        # area filter
        siDoName = self.request.GET.get('siDoName')
        siGunGuName = self.request.GET.get('siGunGuName')
        search_input = self.request.GET.get('search_input')
        if siDoName:
            context['care_list'] = Care.objects.filter(
            Q(siDoName__icontains=siDoName)
            ).distinct()
        if siGunGuName:
            context['care_list'] = Care.objects.filter(
            Q(siDoName__icontains=siDoName) &
            Q(siGunGuName__icontains=siGunGuName)
            ).distinct()
        if search_input:
            context['care_list'] = Care.objects.filter(
                Q(longTermAdminNm__icontains=search_input) |
                Q(adminPttnName__icontains=search_input) |
                Q(ratingCd__icontains=search_input) |
                Q(siDoName__icontains=search_input) |
                Q(siGunGuName__icontains=search_input) |
                Q(ratingGrade__icontains=search_input)
            ).distinct()
        # pagination
        paginator = Paginator(context['care_list'], self.paginate_by)
        page = self.request.GET.get('page','1')
        context['care_list'] = paginator.get_page(page)

        return context

# deatilView
class CareDetailView(DetailView):
    model = Care # 사용할 메인 model
    template_name = 'care/care_detail.html'  # render할 path
    context_object_name = 'detail_info' # 해당의 view로 넘길 객체 이름

    # def get_queryset(self):
    #     return super().get_queryset()

    # def get_context_data(self, **kwargs):
    #     # context = super(CareListView, self).get_context_data(**kwargs)
    #     # context['address_info'] = Address.objects.all()
    #     return context

