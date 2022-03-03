# MIT License

# Copyright (c) 2022 [FacuFalcone]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pandas as pd

# ?## Path of the file.
PATH = './Pandas_Practice/assets/sanctuary.csv'
JSON_CONFIG_PATH = './Pandas_Practice/assets/sanctuary.json'

config_json = pd.read_json(JSON_CONFIG_PATH)

ID = config_json['Schema']['id']
NAME = config_json['Schema']['name']
COSMOS = config_json['Schema']['cosmos']
ARMOR = config_json['Schema']['armor']
LEVEL = config_json['Schema']['level']
POWER_LV = config_json['Schema']['power_level']

# ?## Reads the file and returns a DataFrame.
zodiac_df = pd.read_csv(PATH)

# ?## take a small portion of the whole DF.
small_df = zodiac_df[0:12]

# !## Addition of a new column.

# ?## Adds a new Series into the small DF.
small_df.loc[12] = [13, 'Facu', 'Pisces', 'Gold', 100, 50000]

# ?## Prints the New DataFrame.
print(f'\n DF with a new row:\n{small_df.dropna()}')

# ?## Creates a new column with the sum of the values of the columns.
small_df['Mean'] = small_df[POWER_LV] + small_df[LEVEL]

# ?## Prints the New DataFrame.
print(f'\nDF with a new column:\n{small_df.dropna()}')

# !## Deletion of a column.

# *## Dropping a column.
small_df.drop(columns=[ID], inplace=True)
print(f'\nDF without the id column:\n{small_df}')

# *## Dropping a row.
small_df.drop(index=[12], inplace=True)
print(f'\nDF without the row 12:\n{small_df}')