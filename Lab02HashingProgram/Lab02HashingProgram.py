import os
import hashlib
import json

def hash_file(file_path):
    sha256_hash_alg = hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                sha256_hash_alg.update(chunk)
        return sha256_hash_alg.hexdigest()

    except Exception as e:
        print(f"Error hashing file {file_path}: {e}")
        return None
    
    