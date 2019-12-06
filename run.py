import pycatastro
from pyproj import Proj, transform
import pandas as pd
import json
import collections

# This invokes the wrapper
cat = pycatastro.PyCatastro

# File to load
file_name = input("What's the name of the CSV file to load?: ")
# Load the file onto a Pandas DataFrame
df = pd.read_csv(file_name)

# Obtain the actual strings for provinces
# dic_prov = pd.DataFrame(provincias['consulta_provinciero']['provinciero']['prov'])
# dic_prov.to_csv('diccionario_provincias.csv')

# Apply class method 'catastro' via lambda function
df['result'] = df.apply(lambda x: cat.Consulta_CPMRC(x['PROVINCIA_OK'],'','', x['RC14']), axis=1)

# Declare the output geotag codes
outProj = Proj(init='epsg:4326')

df['longitude'] = df.apply(lambda row: row['result']['consulta_coordenadas']['coordenadas']['coord']['geo']['xcen'], axis=1)
df['latitude'] = df.apply(lambda row: row['result']['consulta_coordenadas']['coordenadas']['coord']['geo']['ycen'], axis=1)
df['epsg'] = df.apply(lambda row: row['result']['consulta_coordenadas']['coordenadas']['coord']['geo']['srs'], axis=1)
df['geotag'] = df.apply(lambda t: transform(t['epsg'],outProj,t['longitude'],t['latitude']), axis=1)
df['gmaps'] = df.apply(lambda r: r['geotag'][::-1], axis=1)
df['dir_cat'] = df.apply(lambda row: row['result']['consulta_coordenadas']['coordenadas']['coord']['ldt'], axis=1)
print(df)

# Export results to CSV
df.to_csv('export.csv')