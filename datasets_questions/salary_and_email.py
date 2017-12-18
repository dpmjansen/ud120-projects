import explore_enron_data as enron

data = enron.enron_data

quant_salary = 0
quant_email = 0

for key, value in data.iteritems() :
    if data[key]['salary'] != 'NaN':
        quant_salary += 1
    if data[key]['email_address'] != 'NaN':
        quant_email += 1
print('Count salary: ' + str(quant_salary))
print('Count email: ' + str(quant_email))
