#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

data_dict.pop('TOTAL',0)

for key in data_dict:
    if(str(data_dict[key]["salary"]) != 'NaN'):
        if(data_dict[key]["salary"] > 1000000):
            print(key + ": "+ "salary: {} bonus: {}".format(str(data_dict[key]["salary"]),str(data_dict[key]["bonus"])))

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter( salary, bonus )

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()


