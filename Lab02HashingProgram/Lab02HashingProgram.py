import os
import hashlib
import json
from pathlib import Path

def hash_file(file_path, algorithm="sha256"):
    hash_function = hashlib.new(algorithm)
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                hash_function.update(chunk)
        return hash_function.hexdigest()

    except Exception as e:
        print(f"Error hashing file {file_path}: {e}")
        return None
    
def traverse_directory(dir_path):
    hash_table = {}
    for root, _, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            if file_hash:
                hash_table[file_path] = file_hash
    return hash_table

