from pandas import DataFrame, to_numeric
from sodapy import Socrata

from os import getenv

client = Socrata(getenv("SOURCE_HOST"), None)

def get_data():
    results = client.get(getenv("SOURCE_FILE"))
    data_frame = DataFrame.from_records(results)
    data_frame['num_resolucion'] = to_numeric(data_frame['num_resolucion'])
    data_frame['cod_territorio'] = to_numeric(data_frame['cod_territorio'])
    data_frame['cantidad'] = to_numeric(data_frame['cantidad'])
    return data_frame