# Problem 2
# The program reads csv file and displays residents of ontario


import pandas as pd

residents = pd.read_csv(r'data/address - address.csv')
ontario_residents = residents[residents['Province'] == 'Ontario']
print(ontario_residents)