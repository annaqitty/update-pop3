import pandas as pd
import numpy as np

def transform_server(server):
    if pd.isna(server):
        return server  # Return NaN as is
    if server.startswith('pop.'):
        return server.replace('pop.', 'pop3.', 1)
    elif server.startswith('pop3.'):
        return server.replace('pop3.', 'pop.', 1)
    else:
        return server

def process_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    
    for index, row in df.iterrows():
        original_server = row['Server']
        transformed_server = transform_server(original_server)
        if transformed_server != original_server:
            print(f"Updating Server: Domain={row['Domain']}, Original Server={original_server}, New Server={transformed_server}, Port={row['Port']}, Socket={row['Socket']}")
            df.at[index, 'Server'] = transformed_server
        else:
            print(f"Read Line: Domain={row['Domain']}, Server={original_server}, Port={row['Port']}, Socket={row['Socket']}")
    
    df.to_csv(output_csv, index=False)

input_csv = 'POP.csv'
output_csv = 'update_server.csv'

process_csv(input_csv, output_csv)
