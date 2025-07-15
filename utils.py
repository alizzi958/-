def read_excel(file_path):
    import pandas as pd
    return pd.read_excel(file_path)

def write_excel(dataframe, file_path):
    import pandas as pd
    dataframe.to_excel(file_path, index=False)

def merge_duplicates(dataframe, group_by_columns):
    return dataframe.groupby(group_by_columns).sum().reset_index()

def format_data(dataframe):
    # Implement any necessary formatting for output
    return dataframe

def get_unique_items(dataframe, column_name):
    return dataframe[column_name].unique()