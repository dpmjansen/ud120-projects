import explore_enron_data as enron

data = enron.enron_data

total = 0
nan = 0

for key, value in data.iteritems() :
    total += 1
    if data[key]['total_payments'] == 'NaN':
        nan += 1

print('NaN total_payments: ' + str(nan))
perc = float(nan)/float(total)
perc *= 100
print('NaN% of total: ' + str(perc))
