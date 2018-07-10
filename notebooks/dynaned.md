

```python
import pandas as pd
import numpy as np
```


```python
ls data/sports_scores/
```

    [0m[01;32mastros_1A10.csv[0m*   [01;32mRice_10H80.csv[0m*    [01;32mTex_15E40.csv[0m*
    [01;32mdynamo_10H30.csv[0m*  [01;32mrockets_1A10.csv[0m*  [01;32mUH_10H50.csv[0m*



```python
ls data/crime_beats/
```

    [0m[01;32mcrime_10H30_10_17.csv[0m*  [01;32mcrime_10H80_10_17.csv[0m*  [01;32mcrime_1A10_10_17.csv[0m*
    [01;32mcrime_10H50_10_17.csv[0m*  [01;32mcrime_15E40_10_17.csv[0m*



```python
games = 'data/sports_scores/dynamo_10H30.csv'

crime = 'data/crime_beats/crime_10H30_10_17.csv'
```

## scores dataframes


```python
df = pd.read_csv(games,index_col='full_date').sort_index(ascending=True)

## win column
df['win'] =  np.where(df['home_score'] > df['away_score'],1,0)

# only oposing name and win boolean
df = df[['away_team','win']]

# show

df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>away_team</th>
      <th>win</th>
    </tr>
    <tr>
      <th>full_date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-04-01</th>
      <td>Real Salt Lake</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2010-04-10</th>
      <td>LA Galaxy</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2010-04-17</th>
      <td>Chivas USA</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2010-05-01</th>
      <td>Sporting KC</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2010-05-05</th>
      <td>FC Dallas</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## crime dataframe


```python
crime_df = pd.read_csv(crime,index_col='Date').sort_index(ascending=True)

## only crimes after 2009
crime_df = crime_df[crime_df.year >=2010]

# selectd columns
crime_df = crime_df[['OffenseType','Premise','NumOffenses','Hour','weekday']]

# count Offense type given date
date_crimes = crime_df.groupby(crime_df.index)['OffenseType',].count()


## show
date_crimes.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>OffenseType</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-01</th>
      <td>3</td>
    </tr>
    <tr>
      <th>2010-01-02</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2010-01-03</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2010-01-04</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2010-01-05</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



## Days dataframe


```python
days = pd.date_range(start='01/01/2010', end='12/30/2017')
days = pd.DataFrame(days)

days.columns = ['days']
days = days.set_index('days').sort_index(ascending=True)

days.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
    </tr>
    <tr>
      <th>days</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-01</th>
    </tr>
    <tr>
      <th>2010-01-02</th>
    </tr>
    <tr>
      <th>2010-01-03</th>
    </tr>
    <tr>
      <th>2010-01-04</th>
    </tr>
    <tr>
      <th>2010-01-05</th>
    </tr>
  </tbody>
</table>
</div>



## Merge days dataframe and  crimes


```python
calendar_crimes = pd.merge(days,date_crimes,  left_index=True, right_index=True, how='left')
calendar_crimes.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>OffenseType</th>
    </tr>
    <tr>
      <th>days</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-01</th>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2010-01-02</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2010-01-03</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2010-01-04</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2010-01-05</th>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



## Merge calendar_crimes with scores


```python
merge_data = pd.merge(calendar_crimes,df,  left_index=True, right_index=True, how='left')

# change column names
merge_data.columns = ['offenses','away_team','win']

merge_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>offenses</th>
      <th>away_team</th>
      <th>win</th>
    </tr>
    <tr>
      <th>days</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-01</th>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2010-01-02</th>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2010-01-03</th>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2010-01-04</th>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2010-01-05</th>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Display non nans


```python
merge_data.dropna(subset=['away_team', 'win'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>offenses</th>
      <th>away_team</th>
      <th>win</th>
    </tr>
    <tr>
      <th>days</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-04-01</th>
      <td>NaN</td>
      <td>Real Salt Lake</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2010-04-10</th>
      <td>1.0</td>
      <td>LA Galaxy</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-04-17</th>
      <td>2.0</td>
      <td>Chivas USA</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2010-05-01</th>
      <td>2.0</td>
      <td>Sporting KC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2010-05-05</th>
      <td>3.0</td>
      <td>FC Dallas</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-05-22</th>
      <td>4.0</td>
      <td>D.C. United</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2010-05-29</th>
      <td>NaN</td>
      <td>Philadelphia</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-06-26</th>
      <td>1.0</td>
      <td>Colorado</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-07-10</th>
      <td>3.0</td>
      <td>Columbus</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-07-31</th>
      <td>NaN</td>
      <td>NY Red Bulls</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-08-21</th>
      <td>2.0</td>
      <td>Chicago</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2010-09-05</th>
      <td>1.0</td>
      <td>San Jose</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-09-18</th>
      <td>NaN</td>
      <td>Toronto FC</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-10-10</th>
      <td>1.0</td>
      <td>New England</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2011-03-19</th>
      <td>3.0</td>
      <td>Philadelphia</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2011-04-10</th>
      <td>NaN</td>
      <td>Vancouver</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2011-04-17</th>
      <td>1.0</td>
      <td>New England</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2011-04-29</th>
      <td>1.0</td>
      <td>D.C. United</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2011-05-04</th>
      <td>1.0</td>
      <td>Colorado</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2011-05-21</th>
      <td>6.0</td>
      <td>NY Red Bulls</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2011-05-28</th>
      <td>2.0</td>
      <td>FC Dallas</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2011-06-11</th>
      <td>2.0</td>
      <td>Chivas USA</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2011-06-18</th>
      <td>3.0</td>
      <td>Columbus</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2011-07-09</th>
      <td>5.0</td>
      <td>Toronto FC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2011-07-16</th>
      <td>2.0</td>
      <td>Sporting KC</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2011-08-14</th>
      <td>2.0</td>
      <td>Portland</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2011-08-20</th>
      <td>NaN</td>
      <td>Real Salt Lake</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2011-09-17</th>
      <td>1.0</td>
      <td>San Jose</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2011-10-01</th>
      <td>3.0</td>
      <td>Chicago</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2011-10-23</th>
      <td>2.0</td>
      <td>LA Galaxy</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2016-06-18</th>
      <td>8.0</td>
      <td>D.C. United</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2016-07-02</th>
      <td>2.0</td>
      <td>Philadelphia</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2016-07-23</th>
      <td>3.0</td>
      <td>Vancouver</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2016-07-31</th>
      <td>4.0</td>
      <td>San Jose</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2016-08-14</th>
      <td>4.0</td>
      <td>Toronto FC</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2016-08-27</th>
      <td>9.0</td>
      <td>FC Dallas</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2016-09-24</th>
      <td>5.0</td>
      <td>Portland</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2016-09-30</th>
      <td>5.0</td>
      <td>NYCFC</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2016-10-08</th>
      <td>6.0</td>
      <td>Colorado</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2016-10-16</th>
      <td>5.0</td>
      <td>LA Galaxy</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2017-03-04</th>
      <td>NaN</td>
      <td>Seattle</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2017-03-11</th>
      <td>2.0</td>
      <td>Columbus</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2017-04-01</th>
      <td>3.0</td>
      <td>NY Red Bulls</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2017-04-15</th>
      <td>5.0</td>
      <td>Minnesota</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2017-04-22</th>
      <td>NaN</td>
      <td>San Jose</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2017-05-06</th>
      <td>3.0</td>
      <td>Orlando</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2017-05-12</th>
      <td>1.0</td>
      <td>Vancouver</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2017-05-31</th>
      <td>6.0</td>
      <td>Real Salt Lake</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2017-06-23</th>
      <td>6.0</td>
      <td>FC Dallas</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2017-07-05</th>
      <td>2.0</td>
      <td>Montreal</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2017-07-29</th>
      <td>3.0</td>
      <td>Portland</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>1.0</td>
      <td>San Jose</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2017-09-09</th>
      <td>1.0</td>
      <td>Colorado</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2017-09-27</th>
      <td>2.0</td>
      <td>LA Galaxy</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2017-09-30</th>
      <td>6.0</td>
      <td>Minnesota</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2017-10-11</th>
      <td>3.0</td>
      <td>Sporting KC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2017-10-22</th>
      <td>NaN</td>
      <td>Chicago</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2017-10-26</th>
      <td>1.0</td>
      <td>Kansas City</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2017-10-30</th>
      <td>1.0</td>
      <td>Portland Tumbers</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2017-11-21</th>
      <td>1.0</td>
      <td>Seattle</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>137 rows × 3 columns</p>
</div>




```python
merge_data.to_csv('data/final/Dynamo1017_final.csv')
```
