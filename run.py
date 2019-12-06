import pycatastro
from pyproj import Proj, transform
import pandas

# This invokes the wrapper
cat = pycatastro.PyCatastro

# File to load
file_name = input("What's the name of the CSV file to load?: ")

df = pandas.read_csv(file_name)

# Fix the value to the variable
# losMunicipios = cat.ConsultaMunicipio('')
# lasProvincias = cat.ConsultaProvincia()

latlong = cat.Consulta_CPMRC('','','','')

df['result'] = df.apply(lambda x: cat.Consulta_CPMRC(0,0,0,x['RC']),axis=1)

print(df['result'])

#x_coord = latlong['consulta_coordenadas']['coordenadas']['coord']['geo']['xcen']
#y_coord = latlong['consulta_coordenadas']['coordenadas']['coord']['geo']['ycen']

#inProj = Proj(init='epsg:25830')
#outProj = Proj(init='epsg:4326')
#x2,y2 = transform(inProj,outProj,x_coord,y_coord)
#print(y2,x2)