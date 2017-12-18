import explore_enron_data as enron

data = enron.enron_data

count = 0

for key, value in data.iteritems():
    if value["poi"]==1:
        count+=1

print(count)
