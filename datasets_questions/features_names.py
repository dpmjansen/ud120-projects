import explore_enron_data as enron

data = enron.enron_data

print(data.itervalues().next().keys())
