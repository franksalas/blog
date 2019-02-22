---
title: Crime Analysis
date: 2018-02-22
draft: false
keywords: []
description: ""
tags: ['Jupyter']
categories: ['ML']
slug: crime-analysis
comment: false
toc: false
autoCollapseToc: false
postMetaInFooter: false
hiddenFromHomePage: false
reward: false
mathjax: false
mathjaxEnableSingleDollar: false
mathjaxEnableAutoNumber: false
---


![alt text][img1]


In this tutorial, we will load and clean UCR, Uniform Crime Report data for 2017 for the city of Houston, Tx.

The UCR data contained in these reports are presented in a monthly breakdown of Part I crimes for which HPD wrote police reports. The data is furthered broken down by police districts and beats and shows descriptions of the following types of crimes:

- Murder
- Rape
- Robbery
- Aggravated assault
- Burglary
- Theft
- Auto theft


<!--more-->
### Breakdown of the data


| Column             | Value    | Description                             | example                              |
|--------------------|----------|-----------------------------------------|-------------------------------------|
| beat               | `string`  | Territory that a police officer patrols | 10H10                               |
| date               | `DateTime`| date when the offense took place       | 4/11/2017 0:00                      |
| hour               | `int`   | time frame when the offense took place      | 15                                  |
| number of offenses | `int`   | if multiple offenses took place         | 1                                   |
| block range        | `str`   | range value of street                   | 2300-2399                           |
| offense type       | `str`   | type of offense form a list             | Theft                               |
| premise            | `str`   | Location type where the offense took place  | Restaurant or Cafeteria Parking Lot |
| street name        | `str`   | Name of the street                      | Canal                               |
| type               | `str`   | Type of street                          | ST                                  |
| suffix             | `str`   | Direction of the street facing               | blank                               |



## Tools & libraries
- Jupyter notebook
- pandas
- numpy
- seaborn
- matplotlib
- glob
- os

# Step 1: Download dataset

Go to https://www.houstontx.gov/police/cs/crime-stats-archives.htm 
and download the excel files for 2017 and save them in your working directory.

It should look something similar to this:
```bash
notebooks/

data/
    clean_data/
        crime/
    crime_data/
        2017/
            jan17.xls
            feb17.xls
            ...
```
- `notebook/` directory is where our jupyter notebook will be
- `data/clean_data/` is where we will save our clean data
- `data/crime_data/2017/` is where the excel files given the year will reside.


Now that we have our data lets start analyzing.


# Step 2 Load Data
Now we will create a notebook and analyze our data


### Load libraries

```python
import pandas as pd
import glob, os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### Combine data and create the data frame

Since we are in a nested directory, we will create a path to our data.

```python
year = '2017'
data_directory = os.path.join('..','data','crime_data/{}'.format(year))
data_directory_saves = os.path.join( '..','data','clean_data','crime/')
```

- `data_directory` creates a path to our crime data folder given the year
- `data_directory_saves` also creates a path but it will be for our finalized clean data


### Combine multiple files

```python
all_files = glob.glob(os.path.join(data_directory, "*.xls")) 
df_from_each_file = (pd.read_excel(f) for f in all_files)
df = pd.concat(df_from_each_file, ignore_index=True)
```
- We  use `glob` to find all the files from our `data_directory` that match the excel extension `.xls`
- create a generator object that reads each excel files into a dataframe
- concat each dataframe into one


### Inspect data

```python
df.info()

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 119727 entries, 0 to 119726
Data columns (total 13 columns):
# offenses      40378 non-null float64
Beat            119727 non-null object
Block Range     79349 non-null object
BlockRange      40378 non-null object
Date            119727 non-null object
Hour            119727 non-null int64
Offense Type    119727 non-null object
Offenses        79349 non-null float64
Premise         119240 non-null object
Street Name     79349 non-null object
StreetName      40378 non-null object
Suffix          119727 non-null object
Type            119727 non-null object
dtypes: float64(2), int64(1), object(10)
memory usage: 11.9+ MB
```

We can see that we have many columns that have similar names, let's check for missing values.

# Step 3 Clean data


### Check  and display missing values


```python
df.apply(lambda x: sum(x.isnull()))
```
```
# offenses      79349
Beat                0
Block Range     40378
BlockRange      79349
Date                0
Hour                0
Offense Type        0
Offenses        40378
Premise           487
Street Name     40378
StreetName      79349
Suffix              0
Type                0
dtype: int64
```

### Display missing values
Create a heatmap of our dataset
```python
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.title('Null dataset display')
plt.show()
```
![](https://i.imgur.com/WDcgdKl.png)

### Results
These columns all have mutual data missing
- `# offenses` & `offenses`
- `Block Range` & `BlockRange`
- `Street Name` & `StreetName`



## Combine similar columns

```python
df['BlockRange'] = pd.concat([df['Block Range'].dropna(),
                              df['BlockRange'].dropna()]).reindex_like(df)

df['StreetName'] = pd.concat([df['Street Name'].dropna(),
                              df['StreetName'].dropna()]).reindex_like(df)

df['# offenses'] = pd.concat([df['# offenses'].dropna(),
                              df['Offenses'].dropna()]).reindex_like(df)
```

- concat similar columns
- only selecting non-nan values
- keeping similar index


![](https://i.imgur.com/jCq31S3.png)

We now see the dataset filled and old columns will be dropped later.



### Lowercase, drop & null value columns
- Lowercase columns make it better to work with 

```python
# Map the lowering function to all column names
df.columns = map(str.lower, df.columns)
```
- renaming columns again makes it easier to work on, especially if the old columns contain a space.. ugh!

```python
df.rename(columns={
    '# offenses': 'num_offenses',
     'offense type': 'offense_type',
    'blockrange': 'block_range',
    'streetname': 'street_name'
}, inplace=True)
```
- here we drop our old columns and some unused


- using `inplace=True` allowes us to do it in one line

```python
df.drop(['suffix','street name','block range','offenses'],axis=1, inplace=True)
```

Let's display or null values now

```python
df.apply(lambda x: sum(x.isnull()))

num_offenses      0
beat              0
block_range       0
date              0
hour              0
offense_type      0
premise         487
street_name       0
type              0
dtype: int64
```
- we see here that `premise` has around 487 null values
- for now lets replace them with `UNK`

```python
df.premise.fillna('UNK',inplace=True)
```


```python
df.head()
```
|    |   num_offenses | beat   | block_range   | date                |   hour | offense_type   | premise                               | street_name   | type   |
|---:|---------------:|:-------|:--------------|:--------------------|-------:|:---------------|:--------------------------------------|:--------------|:-------|
|  0 |              1 | 10H10  | 200-299       | 2017-04-10 00:00:00 |     15 | Burglary       | Residence or House                    | CLIFTON       | -      |
|  1 |              1 | 10H10  | 2300-2399     | 2017-04-11 00:00:00 |     15 | Theft          | Restaurant or Cafeteria Parking Lot   | CANAL         | ST     |
|  2 |              1 | 10H10  | 2300-2399     | 2017-04-11 00:00:00 |     17 | Theft          | Restaurant or Cafeteria Parking Lot   | CANAL         | ST     |
|  3 |              1 | 10H10  | 4600-4699     | 2017-04-12 00:00:00 |      9 | Burglary       | Miscellaneous Business (Non-Specific) | CANAL         | ST     |
|  4 |              1 | 10H10  | 100-199       | 2017-04-12 00:00:00 |     19 | Theft          | Other, Unknown, or Not Listed         | ADAM          | LN     |



## Step 4 Clean.. some more
Now we will check some column and validate the data

### `num_offenses`

```python
df.num_offenses.dtype

dtype('float64')
```
```python
df.num_offenses.value_counts(dropna=False)

1.0     117727
2.0       1661
3.0        227
4.0         70
5.0         21
6.0         10
7.0          7
10.0         2
8.0          2
Name: num_offenses, dtype: int64
```
- We can see that our values are showing up as `float`
- let's change it to `int`

```python
df.num_offenses = df.num_offenses.astype('int')
```

```python
df.num_offenses.dtype
dtype('int64')
```


### `beat`

```python
len(df.beat.value_counts(dropna='False'))
237
```
- we can see that we have 237 values for beat
- that is almost double
- let's check



```python
df.beat.unique()

...
      '21I10 ', '21I20 ', '21I40 ', '21I50 ', '21I60 ', '21I70 ',
       '23J50 ', '24C10 ', '24C20 ', '24C30 ', '24C40 ', '24C50 ',
       '24C60 ', '2A10  ', '2A20  ', '2A30  ', '2A40  ', '2A50  ',
       '2A60  ', '3B10  ', '3B30  ', '3B40  ', '3B50  ', '4F10  ',
       '4F20  ', '4F30  ', '5F10  ', '5F20  ', '5F30  ', '5F40  ',
       '6B10  ', '6B20  ', '6B30  ', '6B40  ', '6B50  ', '6B60  ',
       '7C10  ', '7C20  ', '7C30  ', '7C40  ', '7C50  ', '8C10  ',
       '8C20  ', '8C30  ', '8C40  ', '8C50  ', '8C60  ', '9C10  ',
       '9C20  ', '9C30  ', '9C40  ', 'UNK   ']
```
- Many values have extra space
- lets strip empty space


```python
df.beat = df.beat.str.strip()
```

```python
len(df.beat.unique())
120
```

### `date`

```python
df['date'].dtype
dtype('O')
```
- lets change it to datetime

```python
df['date'] = pd.to_datetime(df['date'])
```

```python
df['date'].dtype
dtype('<M8[ns]')
```


### `offense_type`

```python
df.offense_type.value_counts(dropna=False)

Theft                        61411
Burglary                     15713
Aggravated Assault           11156
Robbery                       8956
AutoTheft                     6649
Theft                         6011
Auto Theft                    3874
Burglary                      1371
Rape                          1239
Aggravated Assault            1158
AutoTheft                      978
Robbery                        822
Murder                         235
Rape                           129
Murder                          23
1                                2
Name: offense_type, dtype: int64
```

We can see that we have multiple versions of the same value, let's check deeper.

```python
df.offense_type.unique()
array(['Burglary', 'Theft', 'Robbery', 'Auto Theft', 'Aggravated Assault',
       'Rape', 'Murder', 'AutoTheft', 1, 'Burglary                 ',
       'Robbery                  ', 'Theft                    ',
       'AutoTheft                ', 'Aggravated Assault       ',
       'Rape                     ', 'Murder                   '],
      dtype=object)
```
- we see that empty space


```python
df.offense_type = df.offense_type.str.strip()
```

```python
df.offense_type.unique()

array(['Burglary', 'Theft', 'Robbery', 'Auto Theft', 'Aggravated Assault',
       'Rape', 'Murder', 'AutoTheft', nan], dtype=object)
```

```python
df.offense_type.value_counts(dropna=False)

Theft                 67422
Burglary              17084
Aggravated Assault    12314
Robbery                9778
AutoTheft              7627
Auto Theft             3874
Rape                   1368
Murder                  258
NaN                       2
Name: offense_type, dtype: int64
```
- we have two versions of "auto theft"
-  let's replace the incorrect

```python
df.offense_type.replace({'AutoTheft':'Auto Theft'}, inplace=True)
```

```python
df.offense_type.value_counts(dropna=False)

Theft                 67422
Burglary              17084
Aggravated Assault    12314
Auto Theft            11501
Robbery                9778
Rape                   1368
Murder                  258
NaN                       2
Name: offense_type, dtype: int64
```

### `street_name`

```python
len(df.street_name.value_counts(dropna=False))
21587
```

```python
df.street_name = df.street_name.str.strip()
```


```python
len(df.street_name.value_counts(dropna=False))
18672
```


### Organize columns

```python
# list of column names in ideal order
cols = ['date','hour','beat','offense_type','block_range','street_name','premise','num_offenses','type']

df = df.reindex(columns=cols)
df.head()
```
|    | date                |   hour | beat   | offense_type   | block_range   | street_name   | premise                               |   num_offenses | type   |
|---:|:--------------------|-------:|:-------|:---------------|:--------------|:--------------|:--------------------------------------|---------------:|:-------|
|  0 | 2017-04-10 00:00:00 |     15 | 10H10  | Burglary       | 200-299       | CLIFTON       | Residence or House                    |              1 | -      |
|  1 | 2017-04-11 00:00:00 |     15 | 10H10  | Theft          | 2300-2399     | CANAL         | Restaurant or Cafeteria Parking Lot   |              1 | ST     |
|  2 | 2017-04-11 00:00:00 |     17 | 10H10  | Theft          | 2300-2399     | CANAL         | Restaurant or Cafeteria Parking Lot   |              1 | ST     |
|  3 | 2017-04-12 00:00:00 |      9 | 10H10  | Burglary       | 4600-4699     | CANAL         | Miscellaneous Business (Non-Specific) |              1 | ST     |
|  4 | 2017-04-12 00:00:00 |     19 | 10H10  | Theft          | 100-199       | ADAM          | Other, Unknown, or Not Listed         |              1 | LN     |



### Check for null values

- 9 `street_names`
- 2 `offense_type`

```python
df.apply(lambda x: sum(x.isnull()))
```
```$
date            0
hour            0
beat            0
offense_type    2
block_range     0
street_name     9
premise         0
num_offenses    0
type            0
dtype: int64
```

### Drop null  `street_name`

```python
df.dropna(subset=['street_name'],inplace=True)
```


### investigate `offense_type`

```python
df = df.reset_index(drop=True)  # reset index

df[df.isnull().any(axis=1)]  # display null value rows
```

|   | date  | hour  | beat  | offense_type |block_range |street_name   |premise   |num_offenses   | type  |
|---|---|---|---|---|---|---|---|---|---|
|35772| 2017-02-15 | 23   | 20G40 | NaN          | 1400-1499   | DAIRY ASHFORD | Apartment          | 1            | RD   | 
|38352| 2016-12-31 | 1    | 6B20  | NaN          | 4200-4299   | OAK SHADOWS   | Residence or House | 1            | DR   | 


Let's analyze all the crimes on these two locations.


### Location 1
```python
da = df.street_name =='DAIRY ASHFORD'
br = df.block_range == '1400-1499'

df[da&br].offense_type.value_counts()


Theft       5
Burglary    1
Name: offense_type, dtype: int64
```
- Change the null value to Theft by index location

```python
df.iloc[35772, df.columns.get_loc('offense_type')] = 'Theft'
```


### Location 2

```python
br = df.block_range == '4200-4299'

os = df.street_name =='OAK SHADOWS'
df[os&br].offense_type.value_counts()

Aggravated Assault    1
Robbery               1
Name: offense_type, dtype: int64
```

```python
df[os&br]
```


|       | date                |   hour | beat   | offense_type       | block_range   | street_name   | premise                |   num_offenses | type   |
|------:|:--------------------|-------:|:-------|:-------------------|:--------------|:--------------|:-----------------------|---------------:|:-------|
| 38352 | 2016-12-31 00:00:00 |      1 | 6B20   | nan                | 4200-4299     | OAK SHADOWS   | Residence or House     |              1 | DR     |
| 52209 | 2017-07-20 00:00:00 |     22 | 14D10  | Robbery            | 4200-4299     | OAK SHADOWS   | Service or Gas Station |              1 | DR     |
| 79668 | 2017-03-09 00:00:00 |     13 | 6B20   | Aggravated Assault | 4200-4299     | OAK SHADOWS   | Residence or House     |              1 | DR     |


- we can see that two locations happen on the same beat and premise
- change the null value  to AA

```python
df.iloc[38352, df.columns.get_loc('offense_type')] = 'Aggravated Assault'
```

### Results

```python
df.info()

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 119718 entries, 0 to 119717
Data columns (total 9 columns):
date            119718 non-null datetime64[ns]
hour            119718 non-null int64
beat            119718 non-null object
offense_type    119718 non-null object
block_range     119718 non-null object
street_name     119718 non-null object
premise         119718 non-null object
num_offenses    119718 non-null int64
type            119718 non-null object
dtypes: datetime64[ns](1), int64(2), object(6)
memory usage: 8.2+ MB
```

# Step 4: save data

check our save directory
```python
data_directory_saves

'../data/clean_data/crime/'
```

```python
df.to_csv(data_directory_saves+'crime_2017.csv')
```



## Sources
- [Houston Crime Statistics](https://www.houstontx.gov/police/cs/crime-stats-archives.htm)
- [Uniform Crime Reporting](https://www.fbi.gov/services/cjis/ucr)






[img1]: /images/crime-analysis/crime.png
