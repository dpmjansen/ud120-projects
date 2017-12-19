#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""
import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.preprocessing import MinMaxScaler

def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()

def minMax(data_dict, feature_list):
    """ prints highest and lowest value of a list of features """
    for i in range(len(feature_list)):
        data = featureFormat(data_dict,[feature_list[i]]) # turn the second feature into an array as the method expects it to be...
        low = numpy.nanmin(data)
        high = numpy.amax(data)
        print("feature: {}".format(feature_list[i]))
        print("low: {}".format(low))
        print("high: {}".format(high))

def rescale(features, predict=None):
    """ rescaled single set of features """
    scaler = MinMaxScaler()
    scaler.fit(features)
    scaler.transform(features)
    if predict:
        print("Scaled value for {}: {}".format(predict,scaler.transform(predict)))


### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

# added to find minmum and max value of exercised_stock_options and salary
feature_name1 = "exercised_stock_options"
feature_name2 = "salary"
feature_list = [feature_name1,feature_name2]

minMax(data_dict,feature_list)
data = featureFormat(data_dict,feature_list)
rescale(data,[[1000000,200000]])

### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
#feature_3 = "total_payments"
poi  = "poi"

# features_list = [poi, feature_1, feature_2, feature_3]
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )



### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2).fit(finance_features)
kmeans.predict(finance_features)
pred = kmeans.labels_

### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
