# from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import BadRequest
from django.views.generic import ListView, DetailView
# from django_filters.views import FilterView
from django.db import models
from .models import Care, Address
# from .models import Review
from django.db.models import Q
from django import template


# Create your views here.

class AreaFilter(object):
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(tags__icontains=q)
        return queryset

# 검색 키워드 시
class SearchFilter(object):
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(tags__icontains=q)
        return queryset



# generic

class CareListView(ListView):
    model = Care
    template_name = 'care_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_keywords = self.request.GET.get('keywords', '')
        selected_state_or_city = self.request.GET.get('state_or_city', '')

        if selected_state_or_city:
            queryset = queryset.filter(
                Q(siDoName__icontains=selected_state_or_city) |
                Q(siGunGuName__icontains=selected_state_or_city)
            )
        if search_keywords:
            queryset = queryset.filter(
                ratingCd__longTermAdminCd__longTermAdminNm__adminPttnName__siDoName__siGunGuName__ratingDate__ratingGrade__opRating__safeRating__rightRating__processRating__resultRating__icontain__icontains=search_keywords
            )
        return queryset


# listview
class CareListView(ListView):
    model = Care # 사용할 메인 model
    template_name = 'care/care_list.html'  # render할 path
    context_object_name = 'care_list' # 해당의 view로 넘길  context 객체 이름
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_keywords = self.request.GET.get('', '')
        if search_keywords:
            queryset = queryset.filter(ratingCd__longTermAdminCd__longTermAdminNm__adminPttnName__siDoName__siGunGuName__ratingDate__ratingGrade__opRating__safeRating__rightRating__processRating__resultRating__icontain__icontains=search_keywords)
        return queryset

# # listView - basic
# class CareListView(AreaFilter, SearchFilter, ListView):
#     model = Care # 사용할 메인 model
#     template_name = 'care/care_list.html'  # render할 path
#     context_object_name = 'care_list' # 해당의 view로 넘길  context 객체 이름


#     def get_queryset(self):
#         # original qs
#         qs = super().get_queryset()

#         # 조건 목록
#         area_input = self.request.GET.getlist('areaName', None) # 지역이름
#         search_input = self.request.GET.getlist('search_input', None)  # 검색어에서 들어올 경우,

#         condition = Q()
#         if area_input:
#             condition.add(Q(siDoName__siGunGuName__in=area_input), Q.AND)
#         if search_input:
#             condition.add(Q(ratingCd__longTermAdminCd__longTermAdminNm__adminPttnName__siDoName__siGunGuName__ratingDate__ratingGrade__opRating__safeRating__rightRating__processRating__resultRating__icontains=search_input), Q.AND)

#         cares = Care.objects.filter(condition).distinct()
#         return cares


#         # return Care.objects.order_by('ratingGrade','-ratingCd') if search_input == None else object_list

#     def get_context_data(self, **kwargs):
#         context = super(CareListView, self).get_context_data(**kwargs)
#         context['address_info'] = Address.objects.all()
#         context['siDo_info'] = Address.objects.filter(siGunGuCd__gt=0, DongCd__gt=0).order_by('siDoCd' 'siGunGuCd','DongCd').values()
#         context['q'] = self.request.GET.get('q')
#         context['condition'] = 
#         # context.update({
#         #     'address_info': Address.objects.all(),
#         #     'siDo_info': Address.objects.filter(siGunGuCd__gt=0, DongCd__gt=0).order_by('siDoCd' 'siGunGuCd','DongCd').values(),
#         #     'q' : self.request.GET.get('q'),
#         # })

#         return context


# deatilView
class CareDetailView(DetailView):
    model = Care # 사용할 메인 model
    template_name = 'care/care_detail.html'  # render할 path
    context_object_name = 'detail_info' # 해당의 view로 넘길 객체 이름

    def get_context_data(self, **kwargs):
        context = super(CareListView, self).get_context_data(**kwargs)
        context['address_info'] = Address.objects.all()
        return context

    def get_queryset(self):
        return super().get_queryset()

