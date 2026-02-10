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


def generate_table():
    dir = input("Enter the directory path of the file to hash: ")
    if not os.path.isdir(dir):
        print("Invalid input. The directory path you entered does not exist.")
        return
    
    hash_table = traverse_directory(dir)

    with open("hash_table.json", "w") as json_file:
        json.dump(hash_table, json_file, indent=5)

    print("Hash table generated. Check hash_table.json for results.")


def validate_hash():
    if not os.path.exists("hash_table.json"):
        print("The hash table file was not found. Please generate a hash table first.")
        return
    
    with open("hash_table.json", "r") as json_file:
        stored_hash_table = json.load(json_file)

    dir = input("Enter the directory path of the file to validate: ")
    if not os.path.isdir(dir):
        print("Invalid input. The directory path you entered does not exist.")
        return
    
    curr_hashes = traverse_directory(dir)

    for filepath, stored_hash in stored_hash_table.items():
        if filepath in curr_hashes:
            if curr_hashes[filepath] != stored_hash:
                print(f"File {filepath} is Invalid.")
            else:
                print(f"File {filepath} is Valid.")
        else:
            print(f"File {filepath} is gone. Deleted. Lost to void, never to be see again.")

    for filepath in curr_hashes:
        if filepath not in stored_hash_table:
            print(f"File {filepath} is new. A brand new file. Welcome to the world, little one.")


def main():
    print("\nThis program is designed to hash files, store files, store the file hashes, and present \nthem in a json file. This program also verifies hash values of files in the chosen directory.\n")
    print("Select an option below to proceed.")

if __name__ == "__main__":
    main()