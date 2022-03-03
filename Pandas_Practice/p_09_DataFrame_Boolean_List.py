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

# ?## Assign a indexed DF with the bracket operator to create
# ?## a new DataFrame with 12 rows.
small_df = zodiac_df[0:12]

# ?## Creates a boolean array with many items as the DataFrame's size.
pisces_row = [
    False, False, False, False, False, False, 
    False, False, False, False, False, True
]

# ?## Pass and prints the rown that meets the condition.
print(small_df[pisces_row])