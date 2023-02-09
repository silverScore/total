   


# listview 에서 검색 filter
# class CareSearchView(ListView):
#     model = Care  # care_list.html 에서 사용할 메인 모델
#     ordering  = ['ratingGrade','-ratingCd']  # 정렬 기준 # 등급과 평가 기간(역) 순
#     template_name = 'care/care_list.html'  # render할 path
#     context_object_name = 'care_search' # 해당의 view로 넘길 객체 이름


#     def get_queryset(self):
#         # original qs
#         qs = super().get_queryset()
        
#         # filter by
#         # 시도별
#         siDoName = self.request.GET.getlist('siDoName', None) # 아무 옵션이 없을 때 전체 상품 보여주기
#         # 시군구별
#         siGunGuName = self.request.GET.getlist('siGunGuName', None)
#         # 특정 요양원 id
#         # id = self.request.GET.getlist('id', 0)
#         object_list = Care.objects.filter(
#             Q(title__icontains=query),
#         )
#         return object_list


#     def get(self, request):
#         siDoName = self.request.GET.getlist('siDoName', None) # 아무 옵션이 없을 때 전체 상품 보여주기
#     def get(self, request):
#         # 시도별
#         siDoName = self.request.GET.getlist('siDoName', None) # 아무 옵션이 없을 때 전체 상품 보여주기
#         # 시군구별
#         siGunGuName = self.request.GET.getlist('siGunGuName', None)
#         # 특정 요양원 id
#         # id = self.request.GET.getlist('id', 0)
#         # # care_type = request.GET.getlist('type', None)  # 추후 종류별

#         area_condition = Q()
#         if siDoName:
#             area_condition.add(Q(siGunGuName__siDoName=siDoName), Q.AND)  # id__siGunGuName__siDoName
#         if siGunGuName:
#             area_condition.add(Q(siGunGuName=siGunGuName), Q.AND)  # id__siGunGuName
        
#         # if id:
#         #     area_condition.add(Q(id=id), Q.AND)

#         # area_condition &= Q(id__range = (siDoName,siGunGuName))

#         area_result = Care.objects.filter(area_condition).order_by('ratingGrade','-ratingCd')
        

#     # for multi models
#     def get_context_data(self, **kwargs):
#         context = super(CareListView, self).get_context_data(**kwargs)
#         context.update({
#             'address_info': Address.objects.all(),
#             'siDo_info': Address.objects.filter(siGunGuCd__gt=0, DongCd__gt=0).order_by('siDoCd','siGunGuCd','DongCd').values(),
            
#         })
#         # self.request.
#         return context

#     for queryset
#     def get_queryset(self):
#         return Care.objects.order_by('ratingGrade','-ratingCd') # 등급과 평가 기간(역) 순
#     def get(self, request):
#     siDoName = self.request.GET.getlist('siDoName', None) # 아무 옵션이 없을 때 전체 상품 보여주기
#     siGunGuName = self.request.GET.getlist('siGunGuName', None)
#     id = self.request.GET.getlist('id', None)
#     # care_type = request.GET.getlist('type', None)  # 추후 종류별
#     # size = request.GET.getlist('size', None)

#     area_condition = Q()

#     if siDoName:
#         area_condition.add(Q(id__siGunGuName__siDoName=siDoName), Q.AND)

#     if siGunGuName:
#         area_condition.add(Q(id__siGunGuName=siGunGuName), Q.AND)

#     if id:
#         area_condition.add(Q(detail_category=id), Q.AND)

#     if care_type:
#         area_condition.add(Q(productoption__care_type__in=care_type), Q.AND)
#         products = products.filter(productoption__care_type__in=care_type).distinct()

#     if size:
#         area_condition.add(Q(productoption__size__in=size), Q.AND)

#     cares = Care.objects.filter(area_condition).distinct().order_by('ratingGrade','-ratingCd')

    

    

# class CareListView(ListView):
#     model = Care # 사용할 메인 model
#     template_name = 'care/care_list.html'  # render할 path
#     context_object_name = 'care_list' # 해당의 view로 넘길 객체 이름

#     # 지역별
#     # filter_siDoCd = 
    
#     # def get(self, *args, **kwargs):
#     #     if 

#     def get_context_data(self, **kwargs):
#         context = super(CareListView, self).get_context_data(**kwargs)
#         context["address_info"] = Address.objects.all()
#         context["siDo_info"] = Address.objects.filter(siGunGuCd__gt=0, DongCd__gt=0).order_by('siDoCd','siGunGuCd','DongCd').values()
#         # self.request.
#         return context

#     def get_queryset(self):
#         return Care.objects.order_by('ratingGrade','-ratingCd')

# # # filterView
# class FilterView(ListView):
#     model = Care # 사용할 메인 model
#     template_name = 'care/care_list.html'  # render할 path
#     context_object_name = 'care_list' # 해당의 view로 넘길 객체 이름

#     def get(self, request):
#         siDoName = request.GET.getlist('siDoName', None) # 아무 옵션이 없을 때 전체 상품 보여주기
#         siGunGuName = request.GET.getlist('siGunGuName', None)
#         id = request.GET.getlist('id', None)
#         # care_type = request.GET.getlist('type', None)  # 추후 종류별
#         # size = request.GET.getlist('size', None)

#         area_condition = Q()

#         if siDoName:
#             area_condition.add(Q(id__siGunGuName__siDoName=siDoName), Q.AND)

#         if siGunGuName:
#             area_condition.add(Q(id__siGunGuName=siGunGuName), Q.AND)

#         if id:
#             area_condition.add(Q(detail_category=id), Q.AND)

#         # if care_type:
#         #     area_condition.add(Q(productoption__care_type__in=care_type), Q.AND)
#         #     products = products.filter(productoption__care_type__in=care_type).distinct()

#         # if size:
#         #     area_condition.add(Q(productoption__size__in=size), Q.AND)

#         cares = Care.objects.filter(area_condition).distinct().order_by('ratingGrade','-ratingCd')

