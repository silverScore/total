
import pandas as pd
import sqlite3

# Read csv file.
df = pd.read_csv("../silverScore/care/data/addressNumbers.csv" )

# Connect to (create) database.
database = "db.sqlite3"
conn = sqlite3.connect(database)
dtype={
    # addressNumbers.csv
    "id": "AutoField",
    "regionCd": "IntegerField",
    "regionNm": "CharField",
    "siDoNm": "CharField",
    "siGunGuNm": "CharField",
    "umdNm": "CharField",
    "riNm": "CharField",
    "siDoCd": "IntegerField",
    "siGunGuCd": "IntegerField",
    "DongCd": "IntegerField",
    "riCd": "IntegerField",
}
df.to_sql(name='care_address', con=conn, if_exists='replace', dtype=dtype, index=True, index_label="id")
conn.close()

