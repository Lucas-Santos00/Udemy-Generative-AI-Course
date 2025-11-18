## Creating a new directory
from genericpath import isdir
import os
new_directory='package'
#os.mkdir(new_directory)
#print('Diretório criado!')

# Listando arquivos e diretórios
item=items=os.listdir('.') ## . represents the currente paths
print(item)

# Joining Paths
dir_name='folder'
file_name='files.txt'
full_path=os.path.join(dir_name, file_name)
print(full_path)

# Get all path - os.getcwd()
dir_name='folder'
file_name='files.txt'
full_path=os.path.join(os.getcwd(),dir_name, file_name)
print(full_path)

# Checking if the file exists or not
path='example.txt'
if os.path.exists(path):
    print(f'The path "{path}" exists')
else:
    print(f'The path "{path}" doesnt texists')

# Checking if its a file or a folder
if os.path.isfile(path):
    print('Its a file!')
elif os.path.isdir(path):
    print('Its a folder!')
else:
    print('Its not a folther neither a file')

# Getting the absolute path
relative_path='example.txt'
absolute_path=os.path.abspath(relative_path)
print(absolute_path)
