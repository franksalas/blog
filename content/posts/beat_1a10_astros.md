---
{
  "title": "beat_1A10_Astros",
  "subtitle": "Generic subtitle",
  "date": "2018-07-06",
  "slug": "beat_1a10_astros"
}
---
<!--more-->


```python
import pandas as pd
```

```python
ls sports_data_clean
```

    [0m[01;32mastros_10_17_plo_clean.csv[0m*       [01;32mhou_rockets_10_17_reg_clean.csv[0m*
    [01;32mastros_10_17_reg_clean.csv[0m*       [01;32mnfl_08_17_clean.csv[0m*
    [01;32mdynamo_10_17_plo.csv[0m*             [01;32mnfl10clean.csv[0m*
    [01;32mdynamo_10_17__reg.csv[0m*            [01;32mnfl10yearsfull.csv[0m*
    [01;32mhou_nfl_1017_post.csv[0m*            [01;32mnfl17years_clean.csv[0m*
    [01;32mhou_nfl_1017_reg.csv[0m*             [01;32mnfl17years_PST_clean.csv[0m*
    [01;32mhou_rockets_08_17_clean.csv[0m*      [01;32mrice_08_17_clean.csv[0m*
    [01;32mhou_rockets_10_17_plo_clean.csv[0m*  [01;32muh_08_17_clean.csv[0m*



```python
# 1A10
hou_reg = 'sports_data_clean/astros_10_17_reg_clean.csv'
hou_pos = 'sports_data_clean/astros_10_17_plo_clean.csv'
```

```python
df_reg = pd.read_csv(hou_reg)
df_pos = pd.read_csv(hou_pos)
```

```python
astros_home_reg = df_reg[df_reg.home_away =='HOME']
```

```python
astros_home_pos = df_pos[df_pos.location == 'Minute Maid Park']
```

```python
astros_home_reg
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
      <th>date</th>
      <th>team</th>
      <th>team_score</th>
      <th>home_away</th>
      <th>opposing</th>
      <th>opp_score</th>
      <th>win_lost</th>
      <th>attendance</th>
      <th>season</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2010-04-05</td>
      <td>HOU</td>
      <td>2</td>
      <td>HOME</td>
      <td>SFG</td>
      <td>5</td>
      <td>L</td>
      <td>43836.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2010-04-06</td>
      <td>HOU</td>
      <td>0</td>
      <td>HOME</td>
      <td>SFG</td>
      <td>3</td>
      <td>L</td>
      <td>24237.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2010-04-07</td>
      <td>HOU</td>
      <td>4</td>
      <td>HOME</td>
      <td>SFG</td>
      <td>10</td>
      <td>L</td>
      <td>21599.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2010-04-09</td>
      <td>HOU</td>
      <td>0</td>
      <td>HOME</td>
      <td>PHI</td>
      <td>8</td>
      <td>L</td>
      <td>27288.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2010-04-10</td>
      <td>HOU</td>
      <td>6</td>
      <td>HOME</td>
      <td>PHI</td>
      <td>9</td>
      <td>L</td>
      <td>35138.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2010-04-11</td>
      <td>HOU</td>
      <td>1</td>
      <td>HOME</td>
      <td>PHI</td>
      <td>2</td>
      <td>L</td>
      <td>28619.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2010-04-20</td>
      <td>HOU</td>
      <td>7</td>
      <td>HOME</td>
      <td>FLA</td>
      <td>5</td>
      <td>W</td>
      <td>24135.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2010-04-21</td>
      <td>HOU</td>
      <td>5</td>
      <td>HOME</td>
      <td>FLA</td>
      <td>4</td>
      <td>W</td>
      <td>22607.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2010-04-22</td>
      <td>HOU</td>
      <td>1</td>
      <td>HOME</td>
      <td>FLA</td>
      <td>5</td>
      <td>L</td>
      <td>21802.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2010-04-23</td>
      <td>HOU</td>
      <td>4</td>
      <td>HOME</td>
      <td>PIT</td>
      <td>3</td>
      <td>W</td>
      <td>30018.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2010-04-24</td>
      <td>HOU</td>
      <td>5</td>
      <td>HOME</td>
      <td>PIT</td>
      <td>2</td>
      <td>W</td>
      <td>30562.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2010-04-25</td>
      <td>HOU</td>
      <td>10</td>
      <td>HOME</td>
      <td>PIT</td>
      <td>3</td>
      <td>W</td>
      <td>27210.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2010-04-27</td>
      <td>HOU</td>
      <td>2</td>
      <td>HOME</td>
      <td>CIN</td>
      <td>6</td>
      <td>L</td>
      <td>22467.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2010-04-28</td>
      <td>HOU</td>
      <td>4</td>
      <td>HOME</td>
      <td>CIN</td>
      <td>6</td>
      <td>L</td>
      <td>21035.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2010-04-29</td>
      <td>HOU</td>
      <td>2</td>
      <td>HOME</td>
      <td>CIN</td>
      <td>4</td>
      <td>L</td>
      <td>21493.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2010-05-03</td>
      <td>HOU</td>
      <td>1</td>
      <td>HOME</td>
      <td>ARI</td>
      <td>9</td>
      <td>L</td>
      <td>20370.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2010-05-04</td>
      <td>HOU</td>
      <td>0</td>
      <td>HOME</td>
      <td>ARI</td>
      <td>1</td>
      <td>L</td>
      <td>22661.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2010-05-05</td>
      <td>HOU</td>
      <td>4</td>
      <td>HOME</td>
      <td>ARI</td>
      <td>2</td>
      <td>W</td>
      <td>21030.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2010-05-06</td>
      <td>HOU</td>
      <td>3</td>
      <td>HOME</td>
      <td>ARI</td>
      <td>6</td>
      <td>L</td>
      <td>21019.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2010-05-07</td>
      <td>HOU</td>
      <td>0</td>
      <td>HOME</td>
      <td>SDP</td>
      <td>7</td>
      <td>L</td>
      <td>25586.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2010-05-08</td>
      <td>HOU</td>
      <td>1</td>
      <td>HOME</td>
      <td>SDP</td>
      <td>2</td>
      <td>L</td>
      <td>27038.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2010-05-09</td>
      <td>HOU</td>
      <td>4</td>
      <td>HOME</td>
      <td>SDP</td>
      <td>3</td>
      <td>W</td>
      <td>23526.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>39</th>
      <td>2010-05-19</td>
      <td>HOU</td>
      <td>7</td>
      <td>HOME</td>
      <td>COL</td>
      <td>3</td>
      <td>W</td>
      <td>25200.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>40</th>
      <td>2010-05-20</td>
      <td>HOU</td>
      <td>0</td>
      <td>HOME</td>
      <td>COL</td>
      <td>4</td>
      <td>L</td>
      <td>25932.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>41</th>
      <td>2010-05-21</td>
      <td>HOU</td>
      <td>2</td>
      <td>HOME</td>
      <td>TBR</td>
      <td>1</td>
      <td>W</td>
      <td>27601.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>42</th>
      <td>2010-05-22</td>
      <td>HOU</td>
      <td>2</td>
      <td>HOME</td>
      <td>TBR</td>
      <td>4</td>
      <td>L</td>
      <td>33778.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>43</th>
      <td>2010-05-23</td>
      <td>HOU</td>
      <td>6</td>
      <td>HOME</td>
      <td>TBR</td>
      <td>10</td>
      <td>L</td>
      <td>28801.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>50</th>
      <td>2010-05-31</td>
      <td>HOU</td>
      <td>4</td>
      <td>HOME</td>
      <td>WSN</td>
      <td>14</td>
      <td>L</td>
      <td>34704.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>51</th>
      <td>2010-06-01</td>
      <td>HOU</td>
      <td>8</td>
      <td>HOME</td>
      <td>WSN</td>
      <td>7</td>
      <td>W</td>
      <td>25249.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>52</th>
      <td>2010-06-02</td>
      <td>HOU</td>
      <td>5</td>
      <td>HOME</td>
      <td>WSN</td>
      <td>1</td>
      <td>W</td>
      <td>26736.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1238</th>
      <td>2017-07-31</td>
      <td>HOU</td>
      <td>14</td>
      <td>HOME</td>
      <td>TBR</td>
      <td>7</td>
      <td>W</td>
      <td>24154.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1239</th>
      <td>2017-08-01</td>
      <td>HOU</td>
      <td>4</td>
      <td>HOME</td>
      <td>TBR</td>
      <td>6</td>
      <td>L</td>
      <td>22985.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1240</th>
      <td>2017-08-02</td>
      <td>HOU</td>
      <td>0</td>
      <td>HOME</td>
      <td>TBR</td>
      <td>3</td>
      <td>L</td>
      <td>26722.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1241</th>
      <td>2017-08-03</td>
      <td>HOU</td>
      <td>3</td>
      <td>HOME</td>
      <td>TBR</td>
      <td>5</td>
      <td>L</td>
      <td>23404.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1242</th>
      <td>2017-08-04</td>
      <td>HOU</td>
      <td>16</td>
      <td>HOME</td>
      <td>TOR</td>
      <td>7</td>
      <td>W</td>
      <td>39287.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1243</th>
      <td>2017-08-05</td>
      <td>HOU</td>
      <td>3</td>
      <td>HOME</td>
      <td>TOR</td>
      <td>4</td>
      <td>L</td>
      <td>41950.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1244</th>
      <td>2017-08-06</td>
      <td>HOU</td>
      <td>7</td>
      <td>HOME</td>
      <td>TOR</td>
      <td>6</td>
      <td>W</td>
      <td>36300.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1253</th>
      <td>2017-08-16</td>
      <td>HOU</td>
      <td>9</td>
      <td>HOME</td>
      <td>ARI</td>
      <td>5</td>
      <td>W</td>
      <td>27278.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1254</th>
      <td>2017-08-17</td>
      <td>HOU</td>
      <td>0</td>
      <td>HOME</td>
      <td>ARI</td>
      <td>4</td>
      <td>L</td>
      <td>27949.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1255</th>
      <td>2017-08-18</td>
      <td>HOU</td>
      <td>3</td>
      <td>HOME</td>
      <td>OAK</td>
      <td>1</td>
      <td>W</td>
      <td>30908.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1256</th>
      <td>2017-08-19</td>
      <td>HOU</td>
      <td>3</td>
      <td>HOME</td>
      <td>OAK</td>
      <td>0</td>
      <td>W</td>
      <td>32796.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1257</th>
      <td>2017-08-20</td>
      <td>HOU</td>
      <td>2</td>
      <td>HOME</td>
      <td>OAK</td>
      <td>3</td>
      <td>L</td>
      <td>34011.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1258</th>
      <td>2017-08-22</td>
      <td>HOU</td>
      <td>3</td>
      <td>HOME</td>
      <td>WSN</td>
      <td>4</td>
      <td>L</td>
      <td>23798.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1259</th>
      <td>2017-08-23</td>
      <td>HOU</td>
      <td>6</td>
      <td>HOME</td>
      <td>WSN</td>
      <td>1</td>
      <td>W</td>
      <td>23434.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1260</th>
      <td>2017-08-24</td>
      <td>HOU</td>
      <td>4</td>
      <td>HOME</td>
      <td>WSN</td>
      <td>5</td>
      <td>L</td>
      <td>24761.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1264</th>
      <td>2017-08-29</td>
      <td>HOU</td>
      <td>2</td>
      <td>HOME</td>
      <td>TEX</td>
      <td>12</td>
      <td>L</td>
      <td>3485.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1265</th>
      <td>2017-08-30</td>
      <td>HOU</td>
      <td>1</td>
      <td>HOME</td>
      <td>TEX</td>
      <td>8</td>
      <td>L</td>
      <td>6123.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1266</th>
      <td>2017-08-31</td>
      <td>HOU</td>
      <td>5</td>
      <td>HOME</td>
      <td>TEX</td>
      <td>1</td>
      <td>W</td>
      <td>3385.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1267</th>
      <td>2017-09-02</td>
      <td>HOU</td>
      <td>12</td>
      <td>HOME</td>
      <td>NYM</td>
      <td>8</td>
      <td>W</td>
      <td>30319.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1268</th>
      <td>2017-09-02</td>
      <td>HOU</td>
      <td>4</td>
      <td>HOME</td>
      <td>NYM</td>
      <td>1</td>
      <td>W</td>
      <td>34904.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1269</th>
      <td>2017-09-03</td>
      <td>HOU</td>
      <td>8</td>
      <td>HOME</td>
      <td>NYM</td>
      <td>6</td>
      <td>W</td>
      <td>32065.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1280</th>
      <td>2017-09-15</td>
      <td>HOU</td>
      <td>5</td>
      <td>HOME</td>
      <td>SEA</td>
      <td>2</td>
      <td>W</td>
      <td>28328.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1281</th>
      <td>2017-09-16</td>
      <td>HOU</td>
      <td>8</td>
      <td>HOME</td>
      <td>SEA</td>
      <td>6</td>
      <td>W</td>
      <td>33650.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1282</th>
      <td>2017-09-17</td>
      <td>HOU</td>
      <td>7</td>
      <td>HOME</td>
      <td>SEA</td>
      <td>1</td>
      <td>W</td>
      <td>30247.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1283</th>
      <td>2017-09-19</td>
      <td>HOU</td>
      <td>3</td>
      <td>HOME</td>
      <td>CHW</td>
      <td>1</td>
      <td>W</td>
      <td>23293.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1284</th>
      <td>2017-09-20</td>
      <td>HOU</td>
      <td>4</td>
      <td>HOME</td>
      <td>CHW</td>
      <td>3</td>
      <td>W</td>
      <td>24995.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1285</th>
      <td>2017-09-21</td>
      <td>HOU</td>
      <td>1</td>
      <td>HOME</td>
      <td>CHW</td>
      <td>3</td>
      <td>L</td>
      <td>24283.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1286</th>
      <td>2017-09-22</td>
      <td>HOU</td>
      <td>3</td>
      <td>HOME</td>
      <td>LAA</td>
      <td>0</td>
      <td>W</td>
      <td>34127.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1287</th>
      <td>2017-09-23</td>
      <td>HOU</td>
      <td>6</td>
      <td>HOME</td>
      <td>LAA</td>
      <td>2</td>
      <td>W</td>
      <td>34035.0</td>
      <td>reg</td>
    </tr>
    <tr>
      <th>1288</th>
      <td>2017-09-24</td>
      <td>HOU</td>
      <td>5</td>
      <td>HOME</td>
      <td>LAA</td>
      <td>7</td>
      <td>L</td>
      <td>36756.0</td>
      <td>reg</td>
    </tr>
  </tbody>
</table>
<p>648 rows × 9 columns</p>
</div>




```python
astros_home_pos
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
      <th>date</th>
      <th>time</th>
      <th>location</th>
      <th>team_1</th>
      <th>score_1</th>
      <th>team_2</th>
      <th>score_2</th>
      <th>home_away</th>
      <th>season</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>2015-10-11</td>
      <td>3:10</td>
      <td>Minute Maid Park</td>
      <td>Kansas City</td>
      <td>2</td>
      <td>Houston</td>
      <td>4</td>
      <td>HOME</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015-10-12</td>
      <td>12:07</td>
      <td>Minute Maid Park</td>
      <td>Kansas City</td>
      <td>9</td>
      <td>Houston</td>
      <td>6</td>
      <td>HOME</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2017-10-06</td>
      <td>2pm</td>
      <td>Minute Maid Park</td>
      <td>Boston</td>
      <td>2</td>
      <td>Houston</td>
      <td>8</td>
      <td>HOME</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2017-10-13</td>
      <td>8:00</td>
      <td>Minute Maid Park</td>
      <td>New York</td>
      <td>1</td>
      <td>Houston</td>
      <td>2</td>
      <td>HOME</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2017-10-14</td>
      <td>4:00</td>
      <td>Minute Maid Park</td>
      <td>New York</td>
      <td>1</td>
      <td>Houston</td>
      <td>2</td>
      <td>HOME</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2017-10-20</td>
      <td>8:00</td>
      <td>Minute Maid Park</td>
      <td>New York</td>
      <td>1</td>
      <td>Houston</td>
      <td>7</td>
      <td>HOME</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2017-10-21</td>
      <td>8:00</td>
      <td>Minute Maid Park</td>
      <td>New York</td>
      <td>0</td>
      <td>Houston</td>
      <td>4</td>
      <td>HOME</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2017-10-27</td>
      <td>8:00</td>
      <td>Minute Maid Park</td>
      <td>Los Angeles</td>
      <td>3</td>
      <td>Houston</td>
      <td>5</td>
      <td>HOME</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2017-10-28</td>
      <td>8:00</td>
      <td>Minute Maid Park</td>
      <td>Los Angeles</td>
      <td>6</td>
      <td>Houston</td>
      <td>2</td>
      <td>HOME</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2017-10-29</td>
      <td>8:00</td>
      <td>Minute Maid Park</td>
      <td>Los Angeles</td>
      <td>12</td>
      <td>Houston</td>
      <td>13</td>
      <td>HOME</td>
      <td>plo</td>
    </tr>
  </tbody>
</table>
</div>




```python
astros_home_pos = astros_home_pos[['date','team_2','score_2','home_away','team_1','score_1','season']]



astros_home_pos.rename(columns = {'team_2':'team','score_2':'team_score','team_1':'opposing','score_1':'opp_score'}, inplace=True)
```

```python
astros_home_pos
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
      <th>date</th>
      <th>team</th>
      <th>team_score</th>
      <th>home_away</th>
      <th>opposing</th>
      <th>opp_score</th>
      <th>season</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>2015-10-11</td>
      <td>Houston</td>
      <td>4</td>
      <td>HOME</td>
      <td>Kansas City</td>
      <td>2</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015-10-12</td>
      <td>Houston</td>
      <td>6</td>
      <td>HOME</td>
      <td>Kansas City</td>
      <td>9</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2017-10-06</td>
      <td>Houston</td>
      <td>8</td>
      <td>HOME</td>
      <td>Boston</td>
      <td>2</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2017-10-13</td>
      <td>Houston</td>
      <td>2</td>
      <td>HOME</td>
      <td>New York</td>
      <td>1</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2017-10-14</td>
      <td>Houston</td>
      <td>2</td>
      <td>HOME</td>
      <td>New York</td>
      <td>1</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2017-10-20</td>
      <td>Houston</td>
      <td>7</td>
      <td>HOME</td>
      <td>New York</td>
      <td>1</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2017-10-21</td>
      <td>Houston</td>
      <td>4</td>
      <td>HOME</td>
      <td>New York</td>
      <td>0</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2017-10-27</td>
      <td>Houston</td>
      <td>5</td>
      <td>HOME</td>
      <td>Los Angeles</td>
      <td>3</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2017-10-28</td>
      <td>Houston</td>
      <td>2</td>
      <td>HOME</td>
      <td>Los Angeles</td>
      <td>6</td>
      <td>plo</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2017-10-29</td>
      <td>Houston</td>
      <td>13</td>
      <td>HOME</td>
      <td>Los Angeles</td>
      <td>12</td>
      <td>plo</td>
    </tr>
  </tbody>
</table>
</div>




```python
astros_home_reg = astros_home_reg[['date','team','team_score','home_away','opposing','opp_score' ,'season']]
```

```python
astros_home_reg.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 648 entries, 0 to 1288
    Data columns (total 7 columns):
    date          648 non-null object
    team          648 non-null object
    team_score    648 non-null int64
    home_away     648 non-null object
    opposing      648 non-null object
    opp_score     648 non-null int64
    season        648 non-null object
    dtypes: int64(2), object(5)
    memory usage: 40.5+ KB



```python
astros_home_pos.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 10 entries, 3 to 21
    Data columns (total 7 columns):
    date          10 non-null object
    team          10 non-null object
    team_score    10 non-null int64
    home_away     10 non-null object
    opposing      10 non-null object
    opp_score     10 non-null int64
    season        10 non-null object
    dtypes: int64(2), object(5)
    memory usage: 640.0+ bytes


# join dataframes


```python
frames = [astros_home_pos,astros_home_reg]


astros = pd.concat(frames)
```

```python
#beat_1A10_Astros
```

```python
astros['beat'] = '1A10'
```

```python
astros.head()
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
      <th>date</th>
      <th>team</th>
      <th>team_score</th>
      <th>home_away</th>
      <th>opposing</th>
      <th>opp_score</th>
      <th>season</th>
      <th>beat</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>2015-10-11</td>
      <td>Houston</td>
      <td>4</td>
      <td>HOME</td>
      <td>Kansas City</td>
      <td>2</td>
      <td>plo</td>
      <td>1A10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015-10-12</td>
      <td>Houston</td>
      <td>6</td>
      <td>HOME</td>
      <td>Kansas City</td>
      <td>9</td>
      <td>plo</td>
      <td>1A10</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2017-10-06</td>
      <td>Houston</td>
      <td>8</td>
      <td>HOME</td>
      <td>Boston</td>
      <td>2</td>
      <td>plo</td>
      <td>1A10</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2017-10-13</td>
      <td>Houston</td>
      <td>2</td>
      <td>HOME</td>
      <td>New York</td>
      <td>1</td>
      <td>plo</td>
      <td>1A10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2017-10-14</td>
      <td>Houston</td>
      <td>2</td>
      <td>HOME</td>
      <td>New York</td>
      <td>1</td>
      <td>plo</td>
      <td>1A10</td>
    </tr>
  </tbody>
</table>
</div>




```python
astros.to_csv('sports_data_clean/astros_1A10.csv')
```

```python
ls sports_data_clean/
```

    [0m[01;32mastros_10_17_plo_clean.csv[0m*       [01;32mhou_rockets_10_17_reg_clean.csv[0m*
    [01;32mastros_10_17_reg_clean.csv[0m*       [01;32mnfl_08_17_clean.csv[0m*
    [01;32mastros_1A10.csv[0m*                  [01;32mnfl10clean.csv[0m*
    [01;32mdynamo_10_17_plo.csv[0m*             [01;32mnfl10yearsfull.csv[0m*
    [01;32mdynamo_10_17__reg.csv[0m*            [01;32mnfl17years_clean.csv[0m*
    [01;32mhou_nfl_1017_post.csv[0m*            [01;32mnfl17years_PST_clean.csv[0m*
    [01;32mhou_nfl_1017_reg.csv[0m*             [01;32mrice_08_17_clean.csv[0m*
    [01;32mhou_rockets_08_17_clean.csv[0m*      [01;32muh_08_17_clean.csv[0m*
    [01;32mhou_rockets_10_17_plo_clean.csv[0m*

