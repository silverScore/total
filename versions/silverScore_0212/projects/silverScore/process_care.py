
import pandas as pd
import sqlite3

# Read csv file.
df = pd.read_csv("../silverScore/care/data/rankStatusData.csv")

# Connect to (create) database.
database = "db.sqlite3"
conn = sqlite3.connect(database)
dtype={
    # rankStatusData.csv
    "id": "AutoField",
    "ratingCd": "CharField",
    "longTermAdminCd": "CharField",
    "longTermAdminNm": "CharField",
    "adminPttnName": "CharField",
    "siDoName": "CharField",
    "siGunGuName": "CharField",
    "ratingDate": "DateField",
    "ratingGrade": "CharField",
    "opRating": "IntegerField",
    "safeRating": "IntegerField",
    "rightRating": "IntegerField",
    "processRating": "IntegerField",
    "resultRating": "IntegerField",
}
df.to_sql(name='care_care', con=conn, if_exists='replace', dtype=dtype, index=True, index_label="id")
conn.close()

