import os
import shutil


IMG_DIR_SRC = './images/'
LAB_DIR_SRC = './labels/'

TRAIN_DST = './train/'
VAL_DST = './val/'

train_files = 'train.txt'
test_files = 'test.txt'


with open(train_files, 'r') as infile:
    train_names = infile.read().split()
train_names = [name[name.rfind('/')+1:name.rfind('.')] for name in train_names]

with open(test_files, 'r') as infile:
    test_names = infile.read().split()
test_names = [name[name.rfind('/')+1:name.rfind('.')] for name in test_names]

for name in train_names:
    shutil.copy(IMG_DIR_SRC + name + '.jpg', TRAIN_DST + 'images/' + name + '.jpg')
    shutil.copy(LAB_DIR_SRC + name + '.txt', TRAIN_DST + 'labels/' + name + '.txt')

for name in test_names:
    shutil.copy(IMG_DIR_SRC + name + '.jpg', VAL_DST + 'images/' + name + '.jpg')
    shutil.copy(LAB_DIR_SRC + name + '.txt', VAL_DST + 'labels/' + name + '.txt')



"""

imgFiles = os.listdir(IMG_DIR_SRC)

for f in allfiles:
    shutil.move(source + f, destination + f)
    
"""