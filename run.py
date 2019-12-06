import pycatastro
from pyproj import Proj, transform
import pandas
import json

# This invokes the wrapper
cat = pycatastro.PyCatastro

# File to load
file_name = input("What's the name of the CSV file to load?: ")
# Load the file onto a Pandas DataFrame
df = pandas.read_csv(file_name)

# Apply class method 'catastro' via lambda function
df['result'] = df.apply(lambda x: cat.Consulta_CPMRC(0,0,0,x['RC']),axis=1)
print(df)

#x_coord = latlong['consulta_coordenadas']['coordenadas']['coord']['geo']['xcen']
#y_coord = latlong['consulta_coordenadas']['coordenadas']['coord']['geo']['ycen']

#inProj = Proj(init='epsg:25830')
#outProj = Proj(init='epsg:4326')
#x2,y2 = transform(inProj,outProj,x_coord,y_coord)
#print(y2,x2)