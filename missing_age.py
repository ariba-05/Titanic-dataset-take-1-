import pickle
from feature_format_for_MissingAge import featureFormat, targetFeatureSplit

with open("dataset_forMissingAge(test).pkl", "r") as data_file:
    my_dataset = pickle.load(data_file)

#print my_dataset
features_list=['Age', 'Title','SibSp','Pclass','SibSp']

data,toPredict_data = featureFormat(my_dataset, features_list, sort_keys = True)

labels, features = targetFeatureSplit(data)
labels2, features2 = targetFeatureSplit(toPredict_data)

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.24, random_state=42)


from sklearn.decomposition import PCA
pca=PCA(n_components=4)
pca.fit(features_train)
features_train=pca.transform(features_train)


from sklearn.tree import DecisionTreeRegressor
reg=DecisionTreeRegressor(random_state=1,presort=True)


reg.fit(features_train,labels_train)
features2=pca.transform(features2)
pred=reg.predict(features2)
print pred
print len(pred)


pred=pred[:177]
print len(pred)
DATASET_PICKLE_FILENAME="predicted_ages.pkl"
with open(DATASET_PICKLE_FILENAME, "w") as dataset_outfile:
    pickle.dump(pred, dataset_outfile)



