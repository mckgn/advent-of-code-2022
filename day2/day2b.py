# Day 2 - Part 2 - Rock, Paper, Scissors - Scored based on corrected strategy guide

# Using Pandas, plan on updating with a non Pandas way

import pandas as pd
import numpy as np

x = open('day2/day2_input.txt').read().splitlines()

df = pd.DataFrame({'Matches' : x})

df['Competitor'] = df['Matches'].astype(str).str[0]
df['Outcome'] = df['Matches'].astype(str).str[2]

df = df.replace('A', 'Rock')
df = df.replace('B', 'Paper')
df = df.replace('C', 'Scissors')

df['Outcome'] = np.where(df['Outcome'] == 'Z', 'Win', df['Outcome'])
df['Outcome'] = np.where(df['Outcome'] == 'X', 'Lose', df['Outcome'])
df['Outcome'] = np.where(df['Outcome'] == 'Y', 'Tie', df['Outcome'])

df['Me'] = np.where((df['Outcome'] == 'Win') & (df['Competitor'] == 'Paper'), 'Scissors', '')
df['Me'] = np.where((df['Outcome'] == 'Win') & (df['Competitor'] == 'Rock'), 'Paper', df['Me'])
df['Me'] = np.where((df['Outcome'] == 'Win') & (df['Competitor'] == 'Scissors'), 'Rock', df['Me'])

df['Me'] = np.where((df['Outcome'] == 'Lose') & (df['Competitor'] == 'Paper'), 'Rock', df['Me'])
df['Me'] = np.where((df['Outcome'] == 'Lose') & (df['Competitor'] == 'Rock'), 'Scissors', df['Me'])
df['Me'] = np.where((df['Outcome'] == 'Lose') & (df['Competitor'] == 'Scissors'), 'Paper', df['Me'])

df['Me'] = np.where((df['Outcome'] == 'Tie'), df['Competitor'], df['Me'])

df['Me Points'] = np.where(df['Me'] == 'Rock', 1, 3)
df['Me Points'] = np.where(df['Me'] == 'Paper', 2, df['Me Points'])

df['Outcome Points'] = np.where(df['Outcome'] == 'Win', 6, 3)
df['Outcome Points'] = np.where(df['Outcome'] == 'Lose', 0, df['Outcome Points'])

df['Total'] = df['Me Points'] + df['Outcome Points']

print(df['Total'].sum())