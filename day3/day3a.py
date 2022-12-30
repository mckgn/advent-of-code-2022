# Day 3 - Part 1 - Backpack Reorganization - 

# Using Pandas, plan on updating with a non Pandas way

import pandas as pd
import numpy as np

x = open('day3/day3_input.txt').read().splitlines()

df = pd.DataFrame()

for i in x:
	temp_df = pd.DataFrame({'Compartment 1' : [i[:int(len(i) / 2)]], 'Compartment 2' : [i[int(len(i) / 2):]]})
	df = pd.concat([df, temp_df])

char_split = []
for index, row in df.iterrows():
	a = row['Compartment 1']
	b = row['Compartment 2']
	char_split.append(set(a).intersection(b).pop())

df = df.reset_index().drop(columns=['index'])

df['Common Letter'] = pd.DataFrame(char_split)

import string
upper_list = list(string.ascii_uppercase)
lower_list = list(string.ascii_lowercase)

lower_df = pd.DataFrame()
m = 1
for n in lower_list:
	new_lower_df = pd.DataFrame({'Common Letter' : [n], 'Priority' : [m]})
	lower_df = pd.concat([lower_df, new_lower_df])
	m += 1

upper_df = pd.DataFrame()
o = 27
for p in upper_list:
	new_upper_df = pd.DataFrame({'Common Letter' : [p], 'Priority' : [o]})
	upper_df = pd.concat([upper_df, new_upper_df])
	o += 1

combined_letters = pd.concat([lower_df, upper_df])

print(df.merge(combined_letters)['Priority'].sum())