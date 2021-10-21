import os
import random
import shutil

if os.path.exists("./ImageSetsft/"):  # 如果文件存在
    shutil.rmtree("./ImageSetsft/")
    os.makedirs('./ImageSetsft/')
else:
    os.makedirs('./ImageSetsft/')


test_percent = 0.1
train_percent = 0.8
val_percent = 0.1

xmlfilepath = './xmlft'

total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = list(range(num))

num_val = int(num * val_percent)
num_test = int(num * test_percent)
num_train = int(num * train_percent)


train_list = random.sample(list, num_train)
for i in train_list:
    list.remove(i)

test_list = random.sample(list, num_test)
for i in test_list:
    list.remove(i)

val_list = list



ftest = open('./ImageSetsft/testft.txt', 'w')
ftrain = open('./ImageSetsft/trainft.txt', 'w')
fval = open('./ImageSetsft/valft.txt', 'w')

for i in range(num):
    name = total_xml[i][:-4] + '\n'
    if i in train_list:
        ftrain.write(name)
    elif i in test_list:
        ftest.write(name)
    else:
        fval.write(name)


ftrain.close()
fval.close()
ftest.close()
