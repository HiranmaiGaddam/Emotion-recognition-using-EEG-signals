from sklearn import svm
import numpy as np
train_y = []
train_a = []
test_y = []
test_a = []
z=[]
z1=[]
train_x = np.genfromtxt('train.csv',delimiter=',')
test_x=np.genfromtxt('test.csv',delimiter=',')

train_x = np.array(train_x)
test_x = np.array(test_x)

with open('labels_0.txt') as my_file:
    p=my_file.readlines()

for i in p:
  
    q= i.split()
    if(q!=[]):
      z= float(q[0])
      train_y.append(z)
train_y = np.array(train_y).astype(np.float)
train_y = train_y.astype(np.int)
with open('labelst_0.txt') as myfile:
    p1=myfile.readlines()

for j in p1:
  
    q1= j.split()
    if(q1!=[]):
      z1= float(q1[0])
      test_y.append(z1)
test_y = np.array(test_y).astype(np.float)
test_y = test_y.astype(np.int)


#print "valence",train_y
#print train_x
#print "train_x",train_x
clf = svm.SVC()
clf.fit(train_x, train_y)
with open('labels_1.txt') as my_file1:
    p2=my_file1.readlines()

for k in p2:
  
    q2= k.split()
    if(q2!=[]):
      z2= float(q2[0])
      train_a.append(z2)
train_a = np.array(train_a).astype(np.float)
train_a = train_a.astype(np.int)
with open('labelst_1.txt') as myfile1:
    p3=myfile1.readlines()

for l in p3:
  
    q3= l.split()
    if(q3!=[]):
      z3= float(q3[0])
      test_a.append(z3)
test_a = np.array(test_a).astype(np.float)
test_a = test_a.astype(np.int)
test_a = np.array(test_y).astype(np.float)
test_a = test_y.astype(np.int)


#print "arousal",train_a[1040:1280]
#print "train_x",len(train_x[0:26])
clf1 = svm.SVC()

clf1.fit(train_x, train_a)

predict_al = clf1.predict(test_x)
#print "alrosal",predict_al
predict_val = clf.predict(test_x) 
#print "valence",predict_val 
val_count = al_count = 0
for i in range(len(test_y)):
	if test_y[i] == predict_val[i]:
		val_count = val_count+1
	if test_a[i] == predict_al[i]:
		al_count = al_count+1
print "predicted valence",(float(val_count)/len(test_y))*100
print "predicted arousal",(float(al_count)/len(test_a))*100

# classifier efficiency
'''
predicted valence 98.046875 percentage
predicted arousal 97.890625 percentage

predicted valence 95.0
predicted arousal 96.09375 
'''
# output
'''
predicted valence 17.9166666667
predicted arousal 13.3333333333
'''
#chan = ['Fp1','AF3','F3','F7','FC5','FC1','C3','T7','CP5','CP1','P3','P7','PO3','O1','Oz','Pz','Fp2','AF4','Fz','F4','F8','FC6','FC2','Cz','C4','T8','CP6','CP2','P4','P8','PO4','O2']

