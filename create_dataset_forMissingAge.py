import csv

import pickle

init=[]
keys=[]
dict={}
maha_dict={}

f=open("train - Copy.csv")

for row in csv.reader(f):
    init.append(row)
f.close()
f=open("test.csv")
ctr=0
for row in csv.reader(f):
    if ctr==0:
        pass
    else:
        init.append(row)
    ctr+=1
f.close()
ctr=0
print init
for item in init:

    if ctr==0:
        keys=item
        keys[3]='Title'

    else:
        dict={}
        item[0]=int(item[0])
        if item[0]<=891:
            for i in range(1,12):

                if item[i]=='':
                    item[i]='NaN'

                else:
                    if i in (5,9):
                        item[i]=float(item[i])

                    if i==4:
                        if item[i]=='male':     ##### male=0 female=1 ####
                            item[i]=0
                        if item[i]=='female':
                            item[i]=1
                    if i==11:
                                                ####C=0 Q=1 S=2####
                        if item[i]=='C':
                            item[i]=0
                        if item[i]=='Q':
                            item[i]=1
                        if item[i]=='S':
                            item[i]=2

                    if i in (1,2,6,7):
                        item[i]=int(item[i])

                    if i==3:
                        tmp=item[i].split()
                                                #### Mr.=0 Mrs.=1 Master.=2 Miss.=3 RareTitle=4 ####
                        if tmp[1]=='Mr.':
                            item[i]=0
                        elif tmp[1]=='Mrs.':
                            item[i]=.333333
                        elif tmp[1]=='Master.':
                            item[i]=.666666
                        elif tmp[1]=='Miss.':
                            item[i]=1
                        else:
                            item[i]=4

                    if i==6:
                        fam=item[i]+int(item[i+1])
                        dict['Family_size'] = fam

                    if i==2:
                        if item[i]==1:
                            item[i]=0
                        if item[i] == 2:
                            item[i] = 1
                        if item[i] == 3:
                            item[i] = 2

                dict[keys[i]]=item[i]

            maha_dict[item[0]] = dict

        if item[0]>891:
            keys=['PassengerId', 'Pclass', 'Title', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
            for i in range(1, 11):

                if item[i] == '':
                    item[i] = 'NaN'

                else:
                    if i in (4, 8):
                        item[i] = float(item[i])

                    if i == 3:
                        if item[i] == 'male':  ##### male=0 female=1 ####
                            item[i] = 0
                        if item[i] == 'female':
                            item[i] = 1
                    if i == 10:
                        ####C=0 Q=1 S=2####
                        if item[i] == 'C':
                            item[i] = 0
                        if item[i] == 'Q':
                            item[i] = 1
                        if item[i] == 'S':
                            item[i] = 2

                    if i in (1, 6, 5):
                        item[i] = int(item[i])

                    if i == 2:
                        tmp = item[i].split()
                        #### Mr.=0 Mrs.=1 Master.=2 Miss.=3 RareTitle=4 ####
                        if tmp[1] == 'Mr.':
                            item[i] = 0
                        elif tmp[1] == 'Mrs.':
                            item[i] = .333333
                        elif tmp[1] == 'Master.':
                            item[i] = .666666
                        elif tmp[1] == 'Miss.':
                            item[i] = 1
                        else:
                            item[i] = 4


                    if i == 1:
                        if item[i] == 1:
                            item[i] = 0
                        if item[i] == 2:
                            item[i] = 1
                        if item[i] == 3:
                            item[i] = 2

                dict[keys[i]] = item[i]

            maha_dict[item[0]]=dict

    ctr+=1


print maha_dict
DATASET_PICKLE_FILENAME="dataset_forMissingAge.pkl"
with open(DATASET_PICKLE_FILENAME, "w") as dataset_outfile:
    pickle.dump(maha_dict, dataset_outfile)

