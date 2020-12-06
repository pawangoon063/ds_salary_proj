# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 02:02:33 2020

@author: pawangoon
"""

import glassdoor_scraper as gs
import pandas as pd

df = gs.get_jobs('data scientist', 500, False)

df.to_csv('glassdoor_jobs.csv',index=False)