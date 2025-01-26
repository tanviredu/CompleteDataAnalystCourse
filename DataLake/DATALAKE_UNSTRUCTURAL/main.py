import os
import shutil
import pandas as pd


def ingest_data(src_path,dest_path):
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    print("[+] Ingesting data from {} to {}".format(src_path,dest_path))
    shutil.copytree(src_path,dest_path)

def read_data(file_path):
    print("[*] Reading data from file path : {}".format(file_path))
    print("[*] Checking file format")
    if file_path.endswith(".csv"):
        print("[*] CSV Detected. loading csv loader")
        return pd.read_csv(file_path)
    elif file_path.endswith(".json"):
        print("[*] JSON Detected.loading JSON loader")
        return pd.read_json(file_path)
    else:
        raise ValueError("[-] Unknown Format. exiting")

def perform_data_operation(data,layer):
    print("Performing data operations for {} Layer".format(layer))
    if layer   == "refined":
        data['Processed'] = True
    elif layer == "curated":
        if 'FirstName' in data.columns:
            ## upper case conversion
            ## consider this is a preprocessing
            data['FirstName'] = data['FirstName'].apply(lambda x:x.upper())
    return data


def MainEx():
    project_path     = os.path.dirname(os.path.abspath(__file__))
    data_path        = os.path.join(project_path,"DATA")
    lake_path        = os.path.join(data_path,"lake")
    raw_path         = os.path.join(data_path,"raw")
    refined_path     = os.path.join(data_path,"refined")
    curated_path     = os.path.join(data_path,"curated")
    #print(raw_path)
    #print(refined_path)
    #print(curated_path)

    ## create directory
    for layer_path in [raw_path,refined_path,curated_path]:
        os.makedirs(layer_path,exist_ok=True)

    
    ## first part of the preprocessing we are moving data from lake to raw folder
    ingest_data(lake_path,raw_path)

    for item in os.listdir(raw_path):
        file_path = os.path.join(raw_path,item)
        data = read_data(file_path)
        refined_data = perform_data_operation(data,"refined")
        refined_out_path = os.path.join(refined_path,item)
        print(refined_data)



MainEx()