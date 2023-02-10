# from .models import Address

# # add model to context -> config/setting.py TEMPALTES에 context_processors 에다가 'common.context_processors.add_address_to_context', 추가함
# def add_address_to_context(request):
#     return {
#         'address_info': Address.objects.all(),
#         'siDo_info': Address.objects.filter(siGunGuCd__gt=0, DongCd__gt=0).order_by('siDoCd', 'siGunGuCd','DongCd').values()
#         }