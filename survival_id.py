import pickle
from feature_format import featureFormat, targetFeatureSplit


with open("dataset.pkl", "r") as data_file:
    my_dataset = pickle.load(data_file)

#print my_dataset
features_list=['Survived', 'Pclass', 'Title', 'Sex', 'Age', 'Family_size', 'Ticket', 'Fare', 'Cabin', 'Embarked','Ticket_prefix']

data = featureFormat(my_dataset, features_list, sort_keys = True)

labels, features = targetFeatureSplit(data)
#print features
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.2, random_state=42)




"""
testfeatures=['Survived','Age','Title']                                                                     
testdata=featureFormat(my_dataset,testfeatures,sort_keys=True)



    import matplotlib.pyplot as py
    for point in testdata:
        sibsp=point[1]
        parch=point[2]
        if(point[0]==0):
            py.scatter(parch, sibsp, color="red")
        if(point[0]==1):
            py.scatter(parch, sibsp, color="blue")
    
    py.xlabel("title")
    py.ylabel("age")
    py.show()
    
"""

#from sklearn.decomposition import PCA
#pca=PCA(n_components=10)
#pca.fit(features_train)
#features_train=pca.transform(features_train)
from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(random_state=90,min_samples_split=25,warm_start=True)
clf.fit(features_train,labels_train)
#features_test=pca.transform(features_test)
pred=clf.predict(features_test)




from sklearn.metrics import accuracy_score
acc=accuracy_score(pred,labels_test)
print ('accuracy ',acc)
from sklearn.metrics import recall_score
recall=recall_score(pred,labels_test)
print ('recall: ',recall)
from sklearn.metrics import precision_score
pre=precision_score(pred,labels_test)
print ('precision:',pre)
print ('score:',clf.score(features_test,labels_test))
from sklearn.metrics import f1_score
f1=f1_score(pred,labels_test)
print("f1score:",f1)


##### EVALUATION ###########
PERF_FORMAT_STRING = "\
\tAccuracy: {:>0.{display_precision}f}\tPrecision: {:>0.{display_precision}f}\t\
Recall: {:>0.{display_precision}f}\tF1: {:>0.{display_precision}f}\tF2: {:>0.{display_precision}f}"
RESULTS_FORMAT_STRING = "\tTotal predictions: {:4d}\tTrue positives: {:4d}\tFalse positives: {:4d}\
\tFalse negatives: {:4d}\tTrue negatives: {:4d}"

from sklearn.cross_validation import StratifiedShuffleSplit

cv = StratifiedShuffleSplit(labels, 50, random_state = 42)
print '3'
true_negatives = 0
false_negatives = 0
true_positives = 0
false_positives = 0
ctr=0
for train_idx, test_idx in cv:
    features_train = []
    features_test  = []
    labels_train   = []
    labels_test    = []
    for ii in train_idx:
        features_train.append( features[ii] )
        labels_train.append( labels[ii] )
    for jj in test_idx:
        features_test.append( features[jj] )
        labels_test.append( labels[jj] )
    print (ctr)
    ### fit the classifier using training set, and test on test set
    clf.fit(features_train, labels_train)
    predictions = clf.predict(features_test)
    ctr+=1
    for prediction, truth in zip(predictions, labels_test):
        if prediction == 0 and truth == 0:
            true_negatives += 1
        elif prediction == 0 and truth == 1:
            false_negatives += 1
        elif prediction == 1 and truth == 0:
            false_positives += 1
        elif prediction == 1 and truth == 1:
            true_positives += 1
        else:
            print "Warning: Found a predicted label not == 0 or 1."
            print "All predictions should take value 0 or 1."
            print "Evaluating performance for processed predictions:"
            break
try:
    total_predictions = true_negatives + false_negatives + false_positives + true_positives
    accuracy = 1.0*(true_positives + true_negatives)/total_predictions
    precision = 1.0*true_positives/(true_positives+false_positives)
    recall = 1.0*true_positives/(true_positives+false_negatives)
    f1 = 2.0 * true_positives/(2*true_positives + false_positives+false_negatives)
    f2 = (1+2.0*2.0) * precision*recall/(4*precision + recall)
    print clf
    print PERF_FORMAT_STRING.format(accuracy, precision, recall, f1, f2, display_precision = 5)
    print RESULTS_FORMAT_STRING.format(total_predictions, true_positives, false_positives, false_negatives, true_negatives)
    print ""
except:
    print "Got a divide by zero when trying out:", clf
    print "Precision or recall may be undefined due to a lack of true positive predicitons."
