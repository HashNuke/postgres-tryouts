import json
import sys
import os
import pandas as pd
from sqlalchemy import create_engine

if len(sys.argv) < 2:
  print("Pass the path to the input file as an argument.")
  print("Check README.md for usage.")
  exit(-1)

filepath = sys.argv[1]
inputfile = os.path.join(filepath)
file = open(inputfile, "r")
json_data = file.read()
data = json.loads(json_data)

df = pd.DataFrame.from_dict(data)
df = df.rename(columns={
  'ConstituentID': 'id',
  'DisplayName': 'name',
  'Nationality': 'nationality',
  'Gender': 'gender',
  'ULAN': 'ulan',
  'ArtistBio': 'bio'
})
df = df.drop(columns=['BeginDate', 'EndDate', 'Wiki QID'])


engine = create_engine('postgresql://localhost/tryouts', echo=False)
df.to_sql(name='artists', con=engine, if_exists='append',index=False)

# for row in data:
#   insert_stmt = """INSERT INTO artists (id, name, bio, nationality, gender, ulan)
#   VALUES ({},'{}','{}','{}','{}','{}');
#   """.format(
#     int(row.get('ConstituentID')),
#     json.dumps(row.get('DisplayName')),
#     json.dumps(row.get('ArtistBio')),
#     json.dumps(row.get('Nationality')),
#     json.dumps(row.get('Gender')),
#     json.dumps(row.get('ULAN'))
#   )
#   print(insert_stmt)