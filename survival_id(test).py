import pickle
from feature_format import featureFormat, targetFeatureSplit
from feature_format_test import testFeatureFormat, testTargetFeatureSplit

with open("dataset.pkl", "r") as data_file:
    my_dataset = pickle.load(data_file)
with open("dataset(test).pkl", "r") as data_file:
    test_dataset = pickle.load(data_file)

# print my_dataset
features_list = ['Survived', 'Pclass', 'Title', 'Sex', 'Age', 'Family_size', 'Ticket', 'Fare', 'Cabin', 'Embarked',
                 'Ticket_prefix']
test_features_list = ['Pclass', 'Title', 'Sex', 'Age', 'Family_size', 'Ticket', 'Fare', 'Cabin', 'Embarked',
                 'Ticket_prefix']



data = featureFormat(my_dataset, features_list, sort_keys=True)
test_data = testFeatureFormat(test_dataset,test_features_list,sort_keys=True)

labels, features = targetFeatureSplit(data)
test_features = testTargetFeatureSplit(test_data)
# print features
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

# from sklearn.decomposition import PCA
# pca=PCA(n_components=10)
# pca.fit(features_train)
# features_train=pca.transform(features_train)
from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(random_state=90,min_samples_split=25,warm_start=True)
clf.fit(features_train, labels_train)
# features_test=pca.transform(features_test)
pred = clf.predict(test_features)

print pred

DATASET_PICKLE_FILENAME="predicted_id.pkl"
with open(DATASET_PICKLE_FILENAME, "w") as dataset_outfile:
    pickle.dump(pred, dataset_outfile)