import json
import os
from os.path import isfile, join

input_folder = os.path.join(os.getcwd(),'input')
output_folder = os.path.join(os.getcwd(),'output')

if not os.path.exists(input_folder):
    os.mkdir(input_folder) 

if not os.path.exists(output_folder):
    os.mkdir(output_folder)


count_file = 0
input_files = [f for f in os.listdir(input_folder) if isfile(join(input_folder, f))]
for file_path in input_files:
    extension = file_path.split('.')
    extension = '.' + extension[-1]
    new_file_name = file_path.split('_')
    new_file_name = new_file_name[0] + extension
    os.rename(os.path.join(input_folder, file_path), os.path.join(output_folder,new_file_name))
    
    
    