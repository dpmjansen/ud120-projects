import explore_enron_data as enron

data = enron.enron_data

for key, value in data.iteritems() :
    print(key)
    print(data[key])
