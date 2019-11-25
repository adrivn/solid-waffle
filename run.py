import pycatastro
from pyproj import Proj, transform

# This invokes the wrapper
cat = pycatastro.PyCatastro

# Fix the value to the variable
losMunicipios = cat.ConsultaMunicipio('')
lasProvincias = cat.ConsultaProvincia()

latlong = cat.Consulta_CPMRC('','','','')

x_coord = latlong['consulta_coordenadas']['coordenadas']['coord']['geo']['xcen']
y_coord = latlong['consulta_coordenadas']['coordenadas']['coord']['geo']['ycen']

inProj = Proj(init='epsg:25830')
outProj = Proj(init='epsg:4326')
x2,y2 = transform(inProj,outProj,x_coord,y_coord)
print(y2,x2)