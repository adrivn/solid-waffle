import pycatastro
import pandas as pd
from tqdm import tqdm

# This invokes the wrapper
cat = pycatastro.PyCatastro

tqdm.pandas()

# Obtain the actual strings for provinces
provincias = cat.ConsultaProvincia()
dic_prov = pd.DataFrame(provincias['consulta_provinciero']['provinciero']['prov'])
dic_municipios = dic_prov['np'].progress_apply(lambda x: cat.ConsultaMunicipio(x))
muni = pd.DataFrame(dic_municipios)

muni.to_csv('export_municipios.csv', encoding="utf-8")