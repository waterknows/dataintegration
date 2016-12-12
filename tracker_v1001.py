#The parameters below should be set according to the format of student records documents.
id_col='Student ID' #name of id columns, such as student email
compare_col='Graduation Date' #name of the column used in comparison, i.e. graudation date
filetype='.csv' #file type of stduent records documents

print('Importing modules...')
import os
from datetime import datetime
import pandas as pd
import numpy as np
print('Finish.')
folder=os.path.dirname(os.path.realpath(__file__))
print('The current folder is',folder,'.')
print('Reading %s from the current folder...' %filetype)
d={}
for filename in os.listdir(folder):
    if filename.endswith(filetype): 
        d[filename]=pd.read_csv('%s%s%s'%(folder,'/',filename), encoding = "ISO-8859-1")
        d[filename]['document']=filename
    else:
        continue
print('Finish.')
print('Concatenating documents...')
df=pd.concat(d.values(), ignore_index=True)
print('Finish.')
print('Comparing and calculating...')
df2=df.groupby([id_col])[compare_col].nunique().reset_index()
print('Finish.')
print('Generating report...')
directory='%s%s'%(folder,'/Report')
if not os.path.exists(directory):
    os.makedirs(directory)
t=datetime.now().strftime('%Y%m%d_%H%M%S')
reportname='%s%s'%(t,' Graduation date comparison.csv')
#graudation date change occurs two times or more, then unique values = 3
df[df[id_col].isin(df2[df2[compare_col]>=3][id_col].values.tolist())].sort_values(by=id_col).to_csv(os.path.join(directory,reportname),index=False)
print('Finish.')