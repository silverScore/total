import csv
from care.models import Care, Address
# addressNumbers.csv 의 column인 header는 삭제처리 할 것.
hand = open('C:/silverScore/projects/silverScore/care/data/addressNumbers.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(Address(regionCd = row[0], regionNm = row[1], siDoNm = row[2], siGunGuNm = row[3], umdNm = row[4], riNm = row[5], siDoCd = row[6], siGunGuCd = row[7], DongCd = row[8], riCd = row[9]))
Address.objects.bulk_create(bulk_list)

hand = open('C:/silverScore/projects/silverScore/care/data/rankStatusData.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(Care(ratingCd = row[0], longTermAdminCd = row[1], longTermAdminNm = row[2], adminPttnName = row[3], siDoName = row[4], siGunGuName = row[5], ratingDate = row[6], ratingGrade = row[7], opRating = row[8], safeRating = row[9], rightRating = row[10], processRating = row[11], resultRating = row[12]))
Care.objects.bulk_create(bulk_list)