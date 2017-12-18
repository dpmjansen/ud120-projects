import explore_enron_data as enron

data = enron.enron_data

print(len(data.itervalues().next()))
