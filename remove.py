from pprint import pprint

import pandas as pd
data = pd.read_csv('scraped_email.csv')
lst = str(data['email'])
lst = lst.replace("\"",'')
lst = lst.replace("\n",'')
lst = set(lst.split(','))
lst1 = list(lst)

keep_col = ['email','source']
new_f = data[keep_col]
new_f.to_csv("scraped_emails_nodups.csv", index=False)

