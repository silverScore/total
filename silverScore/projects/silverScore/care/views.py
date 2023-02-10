from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import BadRequest
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .models import Care, Address, Review
from .forms import ReviewForm

# Create your views here.

# listview
class CareListView(ListView):
    model = Care
    template_name = 'care/care_list.html'
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

# detailView
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

# review list
class ReviewListView(ListView):
    model = Review
    template_name = 'care/review_list.html'
    context_object_name = 'review_list'
    ordering = ['-created_at']

# review create
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    fields = ['amKind', 'faClean', 'content']
    template_name = 'care/review_form.html'
    # success_url = reverse_lazy('care_list')

    def form_valid(self, form):
        if form.instance.status != 1:
            raise BadRequest("Invalid request received!")

        review = get_object_or_404(Care, pk = self.kwargs['care_id']) # Review를 쓰기 위해 Care 인스턴스 존재 확인
        # form.instance.care = Care.objects.get(id=self.kwargs['care_id'])
        if review.is_deleted:
            raise Http404

        form.instance.care = review
        form.instance.author = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('care_detail', kwargs={'pk': self.kwargs['care_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['care'] = Care.objects.get(id=self.kwargs['care_id'])

        return context

        # form.instance.care = Care.objects.get(id=self.kwargs['care_id'])
        # form.instance.author = self.request.user

        # return super().form_valid(form)

# review_modify
class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    fields = ['amKind', 'faClean', 'content']
    template_name = 'care/review_form.html'

    def form_valid(self, form):
        if form.instance.status != 1:
            raise BadRequest("Invalid request received!")

        review = get_object_or_404(Care, pk = self.kwargs['care_id']) # Review를 쓰기 위해 Care 인스턴스 존재 확인
        if review.is_deleted:
            raise Http404

        if self.request.user != form.instance.author:
            raise PermissionDenied

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('care_detail', kwargs={'pk': self.kwargs['care_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['care'] = Care.objects.get(id=self.kwargs['care_id'])

        return context

# review delete
class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'care/review_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        review = self.get_object()
        if request.user != review.author:
            raise PermissionDenied

        success_url = reverse_lazy('care_detail', kwargs={'pk': self.kwargs['care_id']})
        review.delete()

        return HttpResponseRedirect(success_url)

