import pandas as pd
import re
import tldextract
df=pd.read_excel("UCI_Clean.xlsx")
## Regular Expression to Retrieve Domain from URL
Subdomain=[]
Domain=[]
Suffix=[]
for row in df["Website"]:
    if pd.isnull(row):
        Subdomain.append("")
        Domain.append("")
        Suffix.append("")
    else:
        Subdomain.append(tldextract.extract(row)[0])
        Domain.append(tldextract.extract(row)[1])
        Suffix.append(tldextract.extract(row)[2]) 
df["Subdomain"]=Subdomain
df["Domain"]=Domain
df["Suffix"]=Suffix
## Generate Sectors from Domain Suffixes
df['Sector']=''
df['Sector'][df['Suffix'].fillna(0).str.contains("com")]='Private'
df['Sector'][df['Suffix'].fillna(0).str.contains("edu")]='Education'
df['Sector'][df['Suffix'].fillna(0).str.contains("gov")]='Government'
df['Sector'][df['Suffix'].fillna(0).str.contains("org")]='Organization'
## Group by Domain and Generate Company Names
df["DomainSuffix"] = df["Domain"].map(str) +"."+df["Suffix"]
df['Length']=df['PlanDetail'].str.len()
df2=df.loc[df.groupby('DomainSuffix')["Length"].idxmin()][['PlanDetail','DomainSuffix']]
df=df.merge(df2,left_on="DomainSuffix",right_on="DomainSuffix",how="left")
df.to_csv('UCI_Clean2.csv',index=False)
