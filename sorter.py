import os
import shutil

def move_file(file_source,file,pathto):
    try:
        shutil.move(file_source+file,pathto)
    except shutil.Error:
        print('File Exist',file)
    



file_source = 'path/of/directory/'

get_files = os.listdir(file_source)


for i in get_files:
    pathto = os.path.join(file_source,i.split('.')[-1])
    try: 
        os.mkdir(pathto)
        move_file(file_source,i,pathto) 
    except OSError as error: 
        move_file(file_source,i,pathto)
    