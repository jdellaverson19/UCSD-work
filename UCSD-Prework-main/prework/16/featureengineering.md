Dummy for binning
```
import numpy as np
df['Binned_group'] = pd.cut(
    df['Num_Vio'],
    bins = [-np.inf,0,2,np.inf,
    labels = [1,2,3]
    ]
)
```
none, 1, 2+

Preview markdown w ctrl shift v or ctrl k v

Feature engineering 2:
Gaps happen for all sorts of reasons (noise, omissions, for whatever reason, due to transformations or w.e)
Care bc some moels can't work w missing data, sign of wider issue, can be useful feature

```
print(df.info())
#useful for finding missing values
print(df.isnull()) 
#null and not null df and col
print(df['whatever].isnull().sum())
print(df.notnull())

```

If random, use listwise deletion/complete case analysis aka if any null exclude record
```
df.dropna(how='any')
df.dropna(subset=['colName']) 
#above is for certain col

```
Deletes valid data points
relies on randomness
reduces information

Most common is to fi use fillna
```
df['ColName'].fillna(value 'na',inplace = True)
df['colnew'] = df['ColName'].notnull()
df.drop(columns=['ColName'])
```

Deleting missing values isn't great for predictive models -- can't delete in test set
Alternatives are eg categorical columns (replace missing values w most commmon or a flag)
numeric: replace w central value? mean or median tend to be good, w caveat of can lead to biased est of var/covar, stderr test statistics
```
print(df['ConvertedSalary'].mean())
df['Whatever'] = df['Whatever'].fillna(df[Whatever].mean())
df['w'] = df['w'].astype('int64')
#\
df['Whatever'] = df['Whatever'].fillna(round(df[Whatever].mean()))

```


Dealing w other data issues

column w monetary value may contain currency signs, commas, etc that prevent pd from reading as numeric
e.g. dtype of salary column, returns object
```
df['w'] df['w'].str.replace(',','')
#Can use str methods because object series
df['w'] = df['w'].astype('float')
pd.to_numeric(df, errors = 'coerce')
```
