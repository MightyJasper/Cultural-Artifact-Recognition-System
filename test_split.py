import os
import re
import math
import random
from shutil import copyfile

source = "/content/drive/MyDrive/dataset"
train_label_dir = "/content/drive/train/MyDrive/label"
train_image_dir = "/content/drive/train/MyDrive/image"
test_label_dir = "/content/drive/test/MyDrive/label"
test_image_dir = "/content/drive/test/MyDrive/image"


if not os.path.exists(train_label_dir):
    os.makedirs(train_label_dir)
if not os.path.exists(test_image_dir):
    os.makedirs(test_image_dir)
if not os.path.exists(train_image_dir):
    os.makedirs(train_image_dir)
if not os.path.exists(test_label_dir):
    os.makedirs(test_label_dir)

images = [f for f in os.listdir(source)
    if re.search(r'([a-zA-Z0-9\s_\\.\-\(\):])+(?i)(.jpg|.jpeg|.png)$', f)]

ratio = 0.1
num_images = len(images)
num_test_images = math.ceil(ratio*num_images)

for i in range(num_test_images):
    idx = random.randint(0, len(images)-1)
    filename = images[idx]
    copyfile(os.path.join(source, filename),
                os.path.join(test_image_dir, filename))

    txt_filename = os.path.splitext(filename)[0]+'.txt'
    copyfile(os.path.join(source, txt_filename), os.path.join(test_label_dir,txt_filename))
    images.remove(images[idx])

for filename in images:
    copyfile(os.path.join(source, filename),
                os.path.join(train_image_dir, filename))

    txt_filename = os.path.splitext(filename)[0]+'.txt'
    copyfile(os.path.join(source, txt_filename),
                os.path.join(train_label_dir, txt_filename))