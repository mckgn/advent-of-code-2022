# Day 2 - Part 1 - Rock, Paper, Scissors - Total score based on strategy guide

# Using Pandas, plan on updating with a non Pandas way

import pandas as pd
import numpy as np

x = open('day2/day2_input.txt').read().splitlines()

df = pd.DataFrame({'Matches' : x})

df['Competitor'] = df['Matches'].astype(str).str[0]
df['Me'] = df['Matches'].astype(str).str[2]

df = df.replace('A', 'Rock')
df = df.replace('B', 'Paper')
df = df.replace('C', 'Scissors')

df = df.replace('X', 'Rock')
df = df.replace('Y', 'Paper')
df = df.replace('Z', 'Scissors')

df['Outcome'] = np.where(df['Me'] == df['Competitor'], 'Tie', 'Lose')
df['Outcome'] = np.where((df['Me'] == 'Rock') & (df['Competitor'] == 'Scissors'), 'Win', df['Outcome'])
df['Outcome'] = np.where((df['Me'] == 'Paper') & (df['Competitor'] == 'Rock'), 'Win', df['Outcome'])
df['Outcome'] = np.where((df['Me'] == 'Scissors') & (df['Competitor'] == 'Paper'), 'Win', df['Outcome'])

df['Me Points'] = np.where(df['Me'] == 'Rock', 1, 3)
df['Me Points'] = np.where(df['Me'] == 'Paper', 2, df['Me Points'])

df['Outcome Points'] = np.where(df['Outcome'] == 'Win', 6, 3)
df['Outcome Points'] = np.where(df['Outcome'] == 'Lose', 0, df['Outcome Points'])

df['Total'] = df['Me Points'] + df['Outcome Points']

print(df['Total'].sum())