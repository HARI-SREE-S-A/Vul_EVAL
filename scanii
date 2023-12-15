import os
import hashlib

def calculate_hash(file_path, block_size=65536):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for block in iter(lambda: file.read(block_size), b''):
            hasher.update(block)
    return hasher.hexdigest()

def check_file_integrity(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_hash(file_path)
            print(f"File: {file_name}, Hash: {file_hash}")

if __name__ == "__main__":
    directory_to_scan = "."  # Change this to the directory you want to scan
    check_file_integrity(directory_to_scan)
