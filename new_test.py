import os
from shutil import copyfile

dir = "/home/ruph/Documents/new_dataset/images"
dest = "../dataset_current/invalid_img"
path = os.listdir(dir)
# path.remove('labels')
label_path=os.listdir("/home/ruph/Documents/new_dataset/labels")
invalid_img = []
count = 0 
for f in path:
    new = f.split('.')
    if new[0]+'.txt' not in label_path:
        # shutil.move(os.path.join(dir,f),dest,copy_function = shutil.copytree)
        invalid_img.append(f)
        copyfile(os.path.join(dir,f),os.path.join(dest,f))
        os.remove(os.path.join(dir,f))
# print(invalid_img)
temp = []
for f in label_path:
    new = f.split('.')
    if new[0] not in [img.split('.')[0] for img in path ]:
        # invalid_img.append(f)
        temp.append(f)
        # copyfile(os.path.join(dir,f),os.path.join(dest,f))
        # os.remove(os.path.join(dir,f))

             
         

# print(len(invalid_img))