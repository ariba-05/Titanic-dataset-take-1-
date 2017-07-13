import csv
import pickle
with open("predicted_id.pkl", "r") as data_file:
    pred = pickle.load(data_file)

tuple1=()
for item in pred:
    tuple.append(item)
tuple2=()
for i in range(892,1310):
    tuple2.append(i)
list=[tuple1,tuple2]

f = open("gender_submission.csv", 'w', newline='')
for item in pred:
    csv.writer(f).writerow(item)
f.close()
print list

