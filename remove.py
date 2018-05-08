import pandas as pd
f=pd.read_csv("scraped_emails.csv")

from collections import OrderedDict
f['emails'] = f.email.str.split().apply(lambda x: OrderedDict.fromkeys(x).keys()).str.join(' ')
keep_col = ['emails','source']
new_f = f[keep_col]
new_f.to_csv("newFileee.csv", index=False)

# new_f['email'].drop_duplicates()




# import csv
#
# reader=csv.reader(open('scraped_email.csv', 'r'), delimiter=',')
# writer=csv.writer(open('myfilewithoutduplicates.csv', 'w'), delimiter=',')
#
# entries = set()
#
# for row in reader:
#    key = (row[0]) # instead of just the last name
#
#    if key not in entries:
#       writer.writerow(row)
#       entries.add(key)