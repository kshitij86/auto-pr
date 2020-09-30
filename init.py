import os
import sys
import random
import string
from time import sleep

#  For testing, might not need later
import shutil

"""
TODOs:
    1. Read from config file, instead of 
    2. Make PRs from here
    3. Add functions to auto-commit 
"""


num_files = int(sys.argv[1])  # Number of garbage files
garbage_len = int(sys.argv[2])  # Length of garbage content in each file

def get_random_string(length):
    """ Generate randdm string of fixed length """
    letters = string.ascii_lowercase
    res_str = ''.join(random.choice(letters) for i in range(length))
    return res_str


def create_files(num_files=1, garbage_len=100):
    """ Create the garbage files in a src/ folder """
    
    # Check if dir exists
    if not os.path.isdir("./src"):
        os.mkdir("src")
    
    # Random file generator
    for i in range(num_files):
        f_path =  f"./src/{get_random_string(10)}.txt" 
        temp = open(f_path, "w+")
        garbage = get_random_string(garbage_len)
        temp.write(garbage)
        temp.close()
    print(f"Garbage generated")
    
def del_src_dir():
    """ Delete src/ dir """
    if os.path.isdir("./src"):
        shutil.rmtree("./src")
        print("Garbage taken out")

def branch_and_pr(no_pr=4):
    """ Create a branch, make a commit and a PR"""
    #br_name = get_random_str(10)
    #os.system(f"git checkout -b ")
    

def main():
    create_files(num_files, garbage_len)
    del_src_dir()

if __name__ == "__main__":
    main()
