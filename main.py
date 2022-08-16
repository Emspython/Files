__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


# Import Modules
import os
import shutil
from zipfile import ZipFile

org_path = os.getcwd()
files_path = os.path.join(org_path, "files")
cache_path = os.path.join(org_path, "files", "cache")
data_path = os.path.join(org_path, "files", "data.zip")

# 1 clean_cache function with no arg


def clean_cache():
    os.chdir(files_path)
    if os.path.isdir(cache_path):
        shutil.rmtree(cache_path)
    os.mkdir("cache")


clean_cache()

# 2 cache zip functions with 2 arg


def cache_zip(zip, cache):
    with ZipFile(zip, "r") as zipObj:
        zipObj.extractall(cache_path)


cache_zip(data_path, cache_path)


# 3 write function no arg and return a list

directory = os.path.abspath(cache_path)


def cached_files():
    cached_files_list = []
    for path in os.listdir(directory):
        full_path = os.path.join(directory, path)
        cached_files_list.append(full_path)
    return cached_files_list


cached_files()

# 4 find the list from cached files


files_list = cached_files()


def find_password(files_list):
    for file in files_list:
        with open(file) as f:
            for line in f:
                if "password" in line:
                    return line.replace("password: ", "").rstrip("\n")


find_password(files_list)