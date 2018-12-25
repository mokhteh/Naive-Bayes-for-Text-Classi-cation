import numpy as np
import math

d=0.1
label = open("train.label")
trn_label = label.read().splitlines()
label.close()
trn_label = [int(x) for x in trn_label]

infile= open("train.data")
trn_file = infile.read().splitlines()
infile.close()
trn=[]
for item in trn_file:
    item_new = list(item.split())
    item_new = [int(x) for x in item_new]
    trn.append(item_new)
del trn_file
m=0
sum_occur=0
for i in range (len(trn)):
    sum_occur += trn[i][2]
    if trn[i][1] > m:
        m=trn[i][1]

n=trn[-1][0]
num_w = np.zeros((20,m))
Ck = np.zeros(20)
i=0
for j in range(len(trn)):
    num_w[trn_label[trn[j][0]-1]-1,trn[j][1]-1] += trn[j][2]
    Ck[trn_label[trn[j][0]-1]-1] += 1
del trn
pw = np.zeros((20,m))

for i in range (20):
    for j in range(m):
        pw[i][j] = (1.0-d)*(num_w[i][j]/float(sum_occur)) + (d/m)
Ck = [x/float(n) for x in Ck]
predict = [0]*20
id_tst=1
max_list = []
infile=open("test.data")
for i in range (967874):
    tst = infile.readline()
    tst=list(tst.split())
    tst = [int(x) for x in tst]
    if tst[0]>id_tst:
        max_index = predict.index(max(predict))
        max_list.append(max_index+1)
        predict=[0]*20
        id_tst +=1
    for j in range (20):
        if tst[1]<53975:
            predict[j] += tst[2]*math.log(pw[j][tst[1]-1])
max_index = predict.index(max(predict))
max_list.append(max_index+1)
infile.close()
infile= open("test.label")
tst_label=infile.read().splitlines()
infile.close()
tst_label = [int(x) for x in tst_label]
counter=0
for i in range(len(tst_label)):
    if tst_label[i] == max_list[i]:
        counter +=1
acc= counter/7505.
print acc
