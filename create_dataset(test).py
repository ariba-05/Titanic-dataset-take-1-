import csv
import os
import pickle

init=[]
keys=[]
dict={}
maha_dict={}
prefix=[]

f=open("test.csv")

for row in csv.reader(f):
    init.append(row)
ctr=0
print init
for item in init:
    #print item
    if ctr==0:
        keys=item
      #  print keys
        keys[2]='Title'
        keys.append('Ticket_prefix')
       # print init
    else:
        dict={}
        item[0]=int(item[0])
        for i in range(1,11):

            if item[i]=='':
                item[i]='NaN'
                if i==7:
                    dict['Ticket_prefix']=-2



            else:
                if i in (4,8):
                    item[i]=float(item[i])

                if i==3:
                    if item[i]=='male':     ##### male=0 female=1 ####
                        item[i]=0
                    if item[i]=='female':
                        item[i]=1
                if i==10:
                                            ####C=0 Q=1 S=2####
                    if item[i]=='C':
                        item[i]=0
                    if item[i]=='Q':
                        item[i]=1
                    if item[i]=='S':
                        item[i]=2

                if i in (1,5,6):
                    item[i]=int(item[i])

                if i==2:
                    tmp=item[i].split()
                                            #### Mr.=0 Mrs.=1 Master.=2 Miss.=3 RareTitle=4 ####
                    if tmp[1]=='Mr.':
                        item[i]=0
                    elif tmp[1]=='Mrs.':
                        item[i]=1
                    elif tmp[1]=='Master.':
                        item[i]=2
                    elif tmp[1]=='Miss.':
                        item[i]=3
                    else:
                        item[i]=4

                if i==5:
                    fam=item[i]+int(item[i+1])
                    dict['Family_size'] = fam

                if i==7:
                    tmp=item[i].split()
                    item[i]=int(tmp[-1])
                    tmp=tmp[:-1]
                    if tmp!=[]:
                        temp=tmp[0]
                        if temp=='PC':
                            val=0                                                                   #'PC': 60, 'C.A.': 41, 'A/5': 21, 'SOTON/OQ': 15, 'STON/O': 12, 'W/C': 10
                        elif temp=='C.A.':
                            val=1
                        elif temp=='A/5':
                            val=2
                        elif temp=='SOTON/OQ':
                            val=3
                        elif temp=='STON/O':
                            val=4
                        elif temp=='W/C':
                            val=5
                        else:
                            val=6
                        dict['Ticket_prefix']=val
                    if tmp==[]:
                        dict['Ticket_prefix']='NaN'

                if i==9:
                    str=item[i]
                    str=str.replace('A', '0.')
                    str =str.replace('B', '1.')
                    str =str.replace('C', '2.')
                    str =str.replace('D', '3.')
                    str =str.replace('E', '4.')
                    str =str.replace('F', '5.')
                    str =str.replace('G', '6.')
                    str=str.split()

                    if len(str)==1:
                        item[i]=float(str[0])
                    if len(str)==2:
                        item[i]=(float(str[0])+float(str[1]))/2
                    if len(str)==3:
                        item[i]=(float(str[0])+float(str[1])+float(str[2]))/3
                    if len(str)==4:
                        item[i]=(float(str[0])+float(str[1])+float(str[2])+float(str[3]))/4





            dict[keys[i]]=item[i]


        maha_dict[item[0]]=dict

    ctr+=1

from collections import Counter
#print Counter(prefix)
print maha_dict
DATASET_PICKLE_FILENAME="dataset(test).pkl"
with open(DATASET_PICKLE_FILENAME, "w") as dataset_outfile:
    pickle.dump(maha_dict, dataset_outfile)