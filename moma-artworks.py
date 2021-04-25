import json, sys, os
import pandas as pd
from sqlalchemy import create_engine

db_url = 'postgresql://localhost/tryouts'
table = 'artworks'

if len(sys.argv) < 2:
  print("Pass the path to the input file as an argument.")
  print("Check README.md for usage.")
  exit(-1)

filepath = sys.argv[1]
inputfile = os.path.join(filepath)
file = open(inputfile, "r")
data = json.loads(file.read())

df = pd.DataFrame.from_dict(data)
df = df.rename(columns={
  'ObjectID': 'id',
  'Title': 'title',
  'ConstituentID': 'artist_ids',
  'Date': 'artwork_year',
  'Classification': 'classification',
  'Department': 'department',
  'DateAcquired': 'date_acquired',
  'URL': 'website_url',
  'ThumbnailURL': 'thumbnail_url'
})

df['date_acquired'] = pd.to_datetime(
  df['date_acquired'],
  format="%Y-%m-%d"
)

drop_columns = [
  'Cataloged',
  'AccessionNumber',
  'Medium',
  'Dimensions',
  'Artist',
  'ArtistBio',
  'CreditLine',
  'Nationality',
  'BeginDate',
  'EndDate',
  'Gender',
  'Height (cm)',
  'Width (cm)',
  'Depth (cm)',
  'Weight (kg)',
  'Diameter (cm)',
  'Length (cm)',
  'Circumference (cm)',
  'Duration (sec.)'
]
df = df.drop(columns=drop_columns)

engine = create_engine(db_url, echo=False)
df.to_sql(
  name=table,
  con=engine,
  if_exists='append',
  index=False
)
