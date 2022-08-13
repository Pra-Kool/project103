import os
import shutil


from_dir = '/Users/selva'
to_dir = '/Users/selva/Desktop'

path1 = from_dir+'/'+to_dir
path2 = to_dir+'/'+'Document_Files'
path3 = to_dir+'/'+'Document_Files'+'/'+file_name


if os.path.exists(path2):
    print('Moving'+file_name+'....')
    shutil.move(path1,path3)
else:
    os.makedirs(path2)
    print('Moving'+file_name+'....')
    shutil.move(path1,path3)
    
list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    name, ext = os.path.splitext(file)

if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
    file_name = path+"/"+file

