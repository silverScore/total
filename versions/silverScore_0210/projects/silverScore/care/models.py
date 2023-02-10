from django.db import models
from django.contrib.auth import get_user_model
from config import settings

# Create your models here.

# 요양원 - Care
# projects/silverScore/care/data/rankStatusData.csv
class Care(models.Model):
    id = models.AutoField(primary_key=True)
    longTermAdminCd = models.CharField(max_length=15)
    longTermAdminNm = models.CharField(max_length=100)
    adminPttnName = models.CharField(max_length=20)
    ratingCd = models.CharField(max_length=15)
    siDoName = models.CharField(max_length=20, blank=True, null=True)
    siGunGuName = models.CharField(max_length=20, blank=True, null=True)
    ratingDate = models.DateField(blank=True, null=True)
    ratingGrade = models.CharField(max_length=1, blank=True, null=True)
    opRating = models.IntegerField(blank=True, null=True)
    safeRating = models.IntegerField(blank=True, null=True)
    rightRating = models.IntegerField(blank=True, null=True)
    processRating = models.IntegerField(blank=True, null=True)
    resultRating = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["ratingDate","ratingGrade"]

    # admin에서 보이기 위함
    def __str__(self):
        return f"{self.id} / 기관명 : {self.longTermAdminNm} / 기관기호 : {self.longTermAdminCd}"


# 주소 - Address
# projects/silverScore/care/data/addressNumbers.csv
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    regionCd = models.IntegerField(blank=True, null=True)
    regionNm = models.CharField(max_length=200, blank=True, null=True)
    siDoNm = models.CharField(max_length=10, blank=True, null=True)
    siGunGuNm = models.CharField(max_length=10, blank=True, null=True)
    umdNm = models.CharField(max_length=10, blank=True, null=True)
    riNm = models.CharField(max_length=10, blank=True, null=True)
    siDoCd = models.IntegerField(blank=True, null=True)
    siGunGuCd = models.IntegerField(blank=True, null=True)
    DongCd = models.IntegerField(blank=True, null=True)
    riCd = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["regionCd"]

    # admin에서 보이기 위함 AddressInfo.object(idx) 에서
    def __str__(self):
        return f"id : {self.id} / 법정동코드 : {self.regionCd} / 지역명 : {self.regionNm}"


# 리뷰 - Review
User = get_user_model()

class Review(models.Model):
    id = models.BigAutoField(primary_key=True)
    amKind = models.SmallIntegerField(default=0)
    faClean = models.SmallIntegerField(default=0)
    content = models.CharField(max_length=1500, blank=True)
    createDate = models.DateTimeField()
    modifyDate = models.DateTimeField(auto_now=True, null=True, blank=True)

#   member = models.ForeignKey(Member, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    longTermAdminCd = models.ForeignKey(Care, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-createDate']

    def __str__(self):
        return f"친절도 : {self.amKind} / 청결도 : {self.faClean} / 내용 : {self.content}"


