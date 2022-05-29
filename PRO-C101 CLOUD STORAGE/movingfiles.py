from logging import root
import os
import shutil
#os.mkdir("C:/Users/MY PC/Downloads/PYTHON/abc")
#os.getcwd()
#is_exists=os.path.exists("C:/Users/MY PC/Downloads/PYTHON/abc")
#print(is_exists)
path=input("ENTER NAME OF THE DICRECTORY")
list_of_files=os.listdir(path)

for file in list_of_files:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=='':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
        #c/python/book1.exe,c/python/exe/book1.exe
    else:
        os.mkdir(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
#root_ext=os.path.splitext(path)
#print("rootname:",root_ext[0])
#print("ext:",root_ext[1])
#print("before copying files:")
#print(os.listdir(path))
#source="abc/123.txt"
#destination="abc/456.txt"
#dest= shutil.copy(source,destination)
#print("after copying files")
#print(os.listdir(path))

