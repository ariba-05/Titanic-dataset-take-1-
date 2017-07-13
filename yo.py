import pickle
import csv
with open("predicted_id.pkl", "r") as data_file:
    pred = pickle.load(data_file)
tuple1=pred
tuple2=[]
list=[]
j=0
#print len(pred)
for i in range(0,len(tuple1)):
    #print int(tuple1[i])
    item=int(tuple1[i])
    list.append(item)

print type(int(tuple1[0]))



for i in range(892,1310):
    tuple2.append(i)
    j+=1
list=[tuple2,list]
rows=zip(*list)
print rows
f=open("submission.csv","w")
for row in rows:
    csv.writer(f).writerow(row)
f.close()