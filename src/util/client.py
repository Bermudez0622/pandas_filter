from pandas import DataFrame, to_numeric, to_datetime
from sodapy import Socrata

from os import getenv

client = Socrata(getenv("SOURCE_HOST"), None)

def get_data():
    results = client.get(getenv("SOURCE_FILE"), limit=10000)
    data_frame = DataFrame.from_records(results)
    data_frame['num_resolucion'] = to_numeric(data_frame['num_resolucion'])
    data_frame['fecha_resolucion'] = to_datetime(data_frame['fecha_resolucion'], infer_datetime_format=True)
    data_frame['cod_territorio'] = to_numeric(data_frame['cod_territorio'])
    data_frame['cantidad'] = to_numeric(data_frame['cantidad'])
    data_frame['fecha_corte'] = to_datetime(data_frame['fecha_corte'], infer_datetime_format=True)
    return data_frame.dropna()