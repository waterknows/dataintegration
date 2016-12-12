import pandas as pd
df=pd.read_excel("EXITUCI.xlsx")
df['EmployerNum']=df['Employer'].str.len()
df['EmployerNum'].fillna(0, inplace=True)
def num(x):
    if x['PlanType'] == 'Employment':
        return 4.0
    elif x['PlanType'] == 'Graduate and Professional School':
        return 3.0
    elif x['PlanType'] == 'Other':
        return 2.0
    elif x['PlanType'] == 'Still Planning':
        return 2.0
    elif x['PlanType'] == 'No Data':
        return 0.0
df['PlanTypeNum'] = df.apply(num, axis=1)
df['Email'] = df['Email'].str.strip().str.lower()
df2=df.groupby('Email', group_keys=False).apply(lambda x: x.ix[x.PlanTypeNum.idxmax()])
df3=df.groupby('Email', group_keys=False).apply(lambda x: x.ix[x.EmployerNum.idxmax()])
df2['Employer']=df3['Employer']
df2.to_excel('BestOutcome.xlsx',index=False)
df3.to_excel('Bestemployer.xlsx',index=False)