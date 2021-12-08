from pandas.core.frame import DataFrame


def get_options(dataframe: DataFrame, key_column: str, value_column: str = None):
    aux = {}
    rows = [key_column]
    if value_column is not None and value_column != key_column:
        rows.append(value_column)
    for data in dataframe[rows].iterrows():
        aux[data[1][key_column]] = data[1][value_column or key_column]
    return aux.items()