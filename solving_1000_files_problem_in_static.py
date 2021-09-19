#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 17:11:43 2021

@author: kmusial
"""

import pandas as pd
df = pd.read_csv('1_2020_total_6299_companies.csv')
a = 1000 *[0] + 1000 * [1] + 1000 *[2] + 1000 * [3] + 1000 *[4] + 1000 * [5] + 299 *[6] 
df['bucket'] = a
df.sort_values(by='company', inplace=True)
df.to_csv('1_2020_total_6299_companies.csv')