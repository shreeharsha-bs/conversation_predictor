import numpy as np
import pandas as pd
import sys

three_grams = pd.read_csv('three_gram_phrases',sep=' ').values
four_grams = pd.read_csv('four_gram_phrases',sep=' ').values
five_grams = pd.read_csv('5_gram_phrases',sep='\t').values

t1=[];t2=[];t3=[];t4=[]
for f in three_grams[:,0]:
	t1+=[f.split('\t')[0]] 
	t2+=[f.split('\t')[1]]

t1p = []
for p in t1:
	t1p+=[10**float(p)]

for f in three_grams[:,1]:
	t3+=[f]

for f in three_grams[:,2]:
	t4+=[f]


f1=[];f2=[];f3=[];f4=[];f5=[]
for f in four_grams[:,0]:
	f1+=[f.split('\t')[0]] 
	f2+=[f.split('\t')[1]]

f1p = []
for p in f1:
	f1p+=[10**float(p)]

for f in four_grams[:,1]:
	f3+=[f]

for f in four_grams[:,2]:
	f4+=[f]

for f in four_grams[:,3]:
	f5+=[f]
#########################################
F1=[];F2=[];F3=[];F4=[];F5=[];F6=[]
#for F in five_grams[:,0]:
F1=list(five_grams[:,0])		#[F.split('\t')[0]] 
#	F2+=[F.split('\t')[1]]

F1p = []
for p in F1:
	F1p+=[10**float(p)]

for F in five_grams[:,1]:
	F3+=[F]

#for F in five_grams[:,2]:
#	F4+=[F]

#for F in five_grams[:,3]:
#	F5+=[F]
#for F in five_grams[:,4]:
#	F6+=[F]


three_gram_cum_sum = np.cumsum(t1p)
four_gram_cum_sum = np.cumsum(f1p)
five_gram_cum_sum = np.cumsum(F1p)

test_3gram = np.random.uniform(0,three_gram_cum_sum[-1],5)
test_4gram = np.random.uniform(0,four_gram_cum_sum[-1],7)
test_5gram = np.random.uniform(0,five_gram_cum_sum[-1],10)
sent_3=[]
sent_4=[]
sent_5=[]
for word in test_3gram:
	sent_3+=[t2[np.where(word>three_gram_cum_sum)[0][-1]]]+[t3[np.where(word>three_gram_cum_sum)[0][-1]]]+[t4[np.where(word>three_gram_cum_sum)[0][-1]]]
for word in test_4gram:
	sent_4+=[f2[np.where(word>four_gram_cum_sum)[0][-1]]]+[f3[np.where(word>four_gram_cum_sum)[0][-1]]]+[f4[np.where(word>four_gram_cum_sum)[0][-1]]]+[f5[np.where(word>four_gram_cum_sum)[0][-1]]]
for word in test_5gram:
	sent_5+=[F3[np.where(word>five_gram_cum_sum)[0][-1]]]

dic1 = {'<unk>':'😂😂😂', '<s>':'', '</s>':''}
dic2 = {'<unk>':'😂😂', '<s>':'', '</s>':''}
dic3 = {'<unk>':'😂', '<s>':'', '</s>':''}
if(np.random.uniform(1,3)>2):
	dic=dic3
elif(np.random.uniform(1,3)<2 and np.random.uniform(1,3)>1):
	dic=dic2
else:
	dic=dic1

sent_5_r = []
for sent in sent_5:
	sent_5_r+=sent.split(' ') 
sent_new_5 = [dic.get(n, n) for n in sent_5_r]
sent_new_4 = [dic.get(n, n) for n in sent_4]
sent_new_3 = [dic.get(n, n) for n in sent_3]

sent_new_3[:] = [item for item in sent_new_3 if item != '']

sent_new_4[:] = [item for item in sent_new_4 if item != '']

sent_new_5[:] = [item for item in sent_new_5 if item != '']


print(*sent_new_5)
#, *sent_new_4, *sent_new_3)


