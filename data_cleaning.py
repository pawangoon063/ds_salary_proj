# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 04:44:28 2020

@author: pawangoon
"""

import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

#salary parsing

df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x:x.split('(')[0])

minus_Kd = salary.apply(lambda x:x.replace('K','').replace('$',''))

df['min salary'] = minus_Kd.apply(lambda x:int(x.split('-')[0]))
df['max salary'] = minus_Kd.apply(lambda x:int(x.split('-')[1]))
df.rename(columns = {'min salary':'min_salary'}, inplace = True)
df.rename(columns = {'max salary':'max_salary'}, inplace = True) 
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#company name text only
df['company_txt'] = df.apply(lambda x:x['Company Name'] if x['Rating']<0 else x['Company Name'][:-1], axis=1)
#state name
df['job_state'] = df['Location'].apply(lambda x:x.split(',')[1])

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)
#age of company
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2020 - x)
#parsing of job description(python etc.)

#parsing of job description (python, etc.)

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
 
#r studio 
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()

#spark 
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#aws 
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

df.columns

#df_out = df.drop(['Unnamed: 0'], axis =1)

#df_out.to_csv('salary_data_cleaned.csv',index = False)
df.to_csv('salary_data_cleaned.csv',index = False)
