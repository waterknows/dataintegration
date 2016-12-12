import pandas as pd
from openpyxl import load_workbook
df=pd.read_excel('Copy of 2016 Senior survey data for CA.xlsx',sheetname='text',skiprows=[1])
#####Prepare
#replace 0-1 coding with labels
def replace(df,col,val1,val2):
    df[col]=df[col].astype(str).apply(lambda x: x.replace(val1,val2))
    #join variable with '-'
def combine(df,cols):
    agg=df[cols].astype(str).apply(lambda x: ' & '.join(x).replace(' & nan','').replace('nan & ','').replace('nan',''),axis=1)
    return agg   
cols=['fall_1','fall_2','fall_14','fall_4','fall_12','fall_5','fall_13','fallo_1','fallo_2','fallo_7','fallo_3','fallo_4','fallo_5','fallo_6']
cols2=['degfall_1','degfall_2','degfall_3','degfall_4','degfall_5','degfall_6','degfall_7','degfall_8','degfall_9','degfall_10','degfall_11','degfall_12','degfall_13']
cols3=['docfall_1','docfall_2','docfall_3','docfall_4','docfall_5','docfall_6']
cols4=['fchoicer_1','fchoicer_2','fchoicer_3','fchoicer_4','fchoicer_5']
cols5=['degadd2_1','degadd2_2','degadd2_3','degadd2_4','degadd2_5','degadd2_6','degadd2_7','degadd2_8','degadd2_9','degadd2_10','degadd2_11','degadd2_12','degadd2_13','degadd2_14','degadd2_15','degadd2_16','degadd2_17','degadd2_19']
val1s=['Working for pay full-time (including self-employment)','Working for pay part-time','Starting my own company or organization','Attending graduate or professional school full-time','Attending graduate or professional school part-time','Enrolled in some other education program (such as completing your current degree or a post-baccalaureate program)','Other','Internship','Military','Freelancing/performing','Family and other caregiving','Traveling ','Undecided ','Other activity']
val2s=['Working Full Time','Working Part Time','Starting Own Company','Full Time GPS','Part Time GPS','Other Academic Program','(Other)','Internship','Military','Freelancing','Family Caregiving','Traveling','Undecided','Specific']
#####Transform
for col,val1,val2 in zip(cols,val1s,val2s):
    replace(df,col,val1,val2)
for col in cols:
    print(df[df[col]!='nan'][col].value_counts())
df['fall']=combine(df,cols)
df['degfall']=combine(df,cols2)
df['docfall']=combine(df,cols3)
df['fchoicer']=combine(df,cols4)
df['degadd2']=combine(df,cols5)
#df.drop(list(set(cols+cols2+cols3+cols4+cols5)-set(['fall_1','degfall_1','docfall_1','fchoicer_1','degadd2_1'])),axis=1,inplace=True)
book = load_workbook('Copy of 2016 Senior survey data for CA.xlsx')
writer = pd.ExcelWriter('2016 Senior survey data for CA.xlsx', engine='openpyxl') 
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
df.to_excel(writer, 'text_modified',index=False)
writer.save()
