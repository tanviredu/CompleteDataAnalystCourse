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
    pass
