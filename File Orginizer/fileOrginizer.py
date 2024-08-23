import os
import shutil

path = input("Enter path:  ")

os.chdir(path)
files  = os.listdir(path)

for file in files: 
    name,ext = os.path.splitext(file)
    ext = ext[1:]

    if os.path.exists(path+'/'+ext): #/home/user/files/example.txt
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file) # /home/user/files/txt/example.txt
    else:
        os.mkdir(path+'/'+ext)
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file) # /home/user/files/txt/example.txt
