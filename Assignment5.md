```python
import pandas as pd
import os
```


```python
df = pd.read_csv("merged2017.csv")
df
```

    C:\Users\sheka\anaconda3\lib\site-packages\IPython\core\interactiveshell.py:3071: DtypeWarning: Columns (1729) have mixed types.Specify dtype option on import or set low_memory=False.
      has_raised = await self.run_ast_nodes(code_ast.body, cell_name,
    




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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>OPEID6</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ACCREDAGENCY</th>
      <th>INSTURL</th>
      <th>NPCURL</th>
      <th>...</th>
      <th>OMENRUP_PARTTIME_POOLED_SUPP</th>
      <th>FTFTPCTPELL</th>
      <th>FTFTPCTFLOAN</th>
      <th>UG12MN</th>
      <th>G12MN</th>
      <th>SCUGFFN</th>
      <th>POOLYRS_FTFTAIDPCT</th>
      <th>FTFTPCTPELL_POOLED_SUPP</th>
      <th>FTFTPCTFLOAN_POOLED_SUPP</th>
      <th>SCUGFFN_POOLED</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100654</td>
      <td>100200</td>
      <td>1002</td>
      <td>Alabama A &amp; M University</td>
      <td>Normal</td>
      <td>AL</td>
      <td>35762</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.7106</td>
      <td>0.7418</td>
      <td>5207.0</td>
      <td>1185.0</td>
      <td>1410.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100663</td>
      <td>105200</td>
      <td>1052</td>
      <td>University of Alabama at Birmingham</td>
      <td>Birmingham</td>
      <td>AL</td>
      <td>35294-0110</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.4009</td>
      <td>0.5488</td>
      <td>13308.0</td>
      <td>9888.0</td>
      <td>1948.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100690</td>
      <td>2503400</td>
      <td>25034</td>
      <td>Amridge University</td>
      <td>Montgomery</td>
      <td>AL</td>
      <td>36117-3553</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.5000</td>
      <td>0.5000</td>
      <td>431.0</td>
      <td>437.0</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>100706</td>
      <td>105500</td>
      <td>1055</td>
      <td>University of Alabama in Huntsville</td>
      <td>Huntsville</td>
      <td>AL</td>
      <td>35899</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.2012</td>
      <td>0.4231</td>
      <td>7519.0</td>
      <td>2378.0</td>
      <td>1203.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>100724</td>
      <td>100500</td>
      <td>1005</td>
      <td>Alabama State University</td>
      <td>Montgomery</td>
      <td>AL</td>
      <td>36104-0271</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.7594</td>
      <td>0.7402</td>
      <td>5229.0</td>
      <td>687.0</td>
      <td>1143.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
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
      <td>...</td>
      <td>...</td>
      <td>...</td>
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
      <th>7107</th>
      <td>48312404</td>
      <td>108163</td>
      <td>1081</td>
      <td>Arizona State University at Yuma</td>
      <td>Yuma</td>
      <td>AZ</td>
      <td>853656900</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7108</th>
      <td>48387801</td>
      <td>4223701</td>
      <td>42237</td>
      <td>Bay Area Medical Academy - San Jose Satellite ...</td>
      <td>San Jose</td>
      <td>CA</td>
      <td>95113</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7109</th>
      <td>48400201</td>
      <td>4228101</td>
      <td>42281</td>
      <td>High Desert Medical College - Bakerfield</td>
      <td>Bakersfield</td>
      <td>CA</td>
      <td>93301</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7110</th>
      <td>48778201</td>
      <td>4221501</td>
      <td>42215</td>
      <td>BCI - Malden</td>
      <td>Malden</td>
      <td>MA</td>
      <td>021480000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7111</th>
      <td>49005401</td>
      <td>4182601</td>
      <td>41826</td>
      <td>HCI College - Fort Lauderdale Campus</td>
      <td>Fort Lauderdale</td>
      <td>FL</td>
      <td>33309</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>7112 rows × 1986 columns</p>
</div>




```python
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>OPEID6</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ACCREDAGENCY</th>
      <th>INSTURL</th>
      <th>NPCURL</th>
      <th>...</th>
      <th>OMENRUP_PARTTIME_POOLED_SUPP</th>
      <th>FTFTPCTPELL</th>
      <th>FTFTPCTFLOAN</th>
      <th>UG12MN</th>
      <th>G12MN</th>
      <th>SCUGFFN</th>
      <th>POOLYRS_FTFTAIDPCT</th>
      <th>FTFTPCTPELL_POOLED_SUPP</th>
      <th>FTFTPCTFLOAN_POOLED_SUPP</th>
      <th>SCUGFFN_POOLED</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100654</td>
      <td>100200</td>
      <td>1002</td>
      <td>Alabama A &amp; M University</td>
      <td>Normal</td>
      <td>AL</td>
      <td>35762</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.7106</td>
      <td>0.7418</td>
      <td>5207.0</td>
      <td>1185.0</td>
      <td>1410.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100663</td>
      <td>105200</td>
      <td>1052</td>
      <td>University of Alabama at Birmingham</td>
      <td>Birmingham</td>
      <td>AL</td>
      <td>35294-0110</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.4009</td>
      <td>0.5488</td>
      <td>13308.0</td>
      <td>9888.0</td>
      <td>1948.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100690</td>
      <td>2503400</td>
      <td>25034</td>
      <td>Amridge University</td>
      <td>Montgomery</td>
      <td>AL</td>
      <td>36117-3553</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.5000</td>
      <td>0.5000</td>
      <td>431.0</td>
      <td>437.0</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>100706</td>
      <td>105500</td>
      <td>1055</td>
      <td>University of Alabama in Huntsville</td>
      <td>Huntsville</td>
      <td>AL</td>
      <td>35899</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.2012</td>
      <td>0.4231</td>
      <td>7519.0</td>
      <td>2378.0</td>
      <td>1203.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>100724</td>
      <td>100500</td>
      <td>1005</td>
      <td>Alabama State University</td>
      <td>Montgomery</td>
      <td>AL</td>
      <td>36104-0271</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.7594</td>
      <td>0.7402</td>
      <td>5229.0</td>
      <td>687.0</td>
      <td>1143.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 1986 columns</p>
</div>




```python
df.tail()
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>OPEID6</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ACCREDAGENCY</th>
      <th>INSTURL</th>
      <th>NPCURL</th>
      <th>...</th>
      <th>OMENRUP_PARTTIME_POOLED_SUPP</th>
      <th>FTFTPCTPELL</th>
      <th>FTFTPCTFLOAN</th>
      <th>UG12MN</th>
      <th>G12MN</th>
      <th>SCUGFFN</th>
      <th>POOLYRS_FTFTAIDPCT</th>
      <th>FTFTPCTPELL_POOLED_SUPP</th>
      <th>FTFTPCTFLOAN_POOLED_SUPP</th>
      <th>SCUGFFN_POOLED</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7107</th>
      <td>48312404</td>
      <td>108163</td>
      <td>1081</td>
      <td>Arizona State University at Yuma</td>
      <td>Yuma</td>
      <td>AZ</td>
      <td>853656900</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7108</th>
      <td>48387801</td>
      <td>4223701</td>
      <td>42237</td>
      <td>Bay Area Medical Academy - San Jose Satellite ...</td>
      <td>San Jose</td>
      <td>CA</td>
      <td>95113</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7109</th>
      <td>48400201</td>
      <td>4228101</td>
      <td>42281</td>
      <td>High Desert Medical College - Bakerfield</td>
      <td>Bakersfield</td>
      <td>CA</td>
      <td>93301</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7110</th>
      <td>48778201</td>
      <td>4221501</td>
      <td>42215</td>
      <td>BCI - Malden</td>
      <td>Malden</td>
      <td>MA</td>
      <td>021480000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7111</th>
      <td>49005401</td>
      <td>4182601</td>
      <td>41826</td>
      <td>HCI College - Fort Lauderdale Campus</td>
      <td>Fort Lauderdale</td>
      <td>FL</td>
      <td>33309</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 1986 columns</p>
</div>




```python
df.sample(5)
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>OPEID6</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ACCREDAGENCY</th>
      <th>INSTURL</th>
      <th>NPCURL</th>
      <th>...</th>
      <th>OMENRUP_PARTTIME_POOLED_SUPP</th>
      <th>FTFTPCTPELL</th>
      <th>FTFTPCTFLOAN</th>
      <th>UG12MN</th>
      <th>G12MN</th>
      <th>SCUGFFN</th>
      <th>POOLYRS_FTFTAIDPCT</th>
      <th>FTFTPCTPELL_POOLED_SUPP</th>
      <th>FTFTPCTFLOAN_POOLED_SUPP</th>
      <th>SCUGFFN_POOLED</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6257</th>
      <td>483610</td>
      <td>4190900</td>
      <td>41909</td>
      <td>Sutter Beauty College</td>
      <td>Yuba City</td>
      <td>CA</td>
      <td>95991</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.8182</td>
      <td>0.0000</td>
      <td>101.0</td>
      <td>NaN</td>
      <td>55.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>720</th>
      <td>135294</td>
      <td>558600</td>
      <td>5586</td>
      <td>Lindsey Hopkins Technical College</td>
      <td>Miami</td>
      <td>FL</td>
      <td>33127</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.5181</td>
      <td>0.0000</td>
      <td>1104.0</td>
      <td>NaN</td>
      <td>581.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1902</th>
      <td>177931</td>
      <td>2142200</td>
      <td>21422</td>
      <td>Lex La-Ray Technical Center</td>
      <td>Lexington</td>
      <td>MO</td>
      <td>64067-1525</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.7273</td>
      <td>0.6364</td>
      <td>49.0</td>
      <td>NaN</td>
      <td>11.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>162</th>
      <td>107558</td>
      <td>109400</td>
      <td>1094</td>
      <td>University of the Ozarks</td>
      <td>Clarksville</td>
      <td>AR</td>
      <td>72830</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.5079</td>
      <td>0.7672</td>
      <td>712.0</td>
      <td>NaN</td>
      <td>189.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5504</th>
      <td>455512</td>
      <td>4143800</td>
      <td>41438</td>
      <td>Woodland Community College</td>
      <td>Woodland</td>
      <td>CA</td>
      <td>95776</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.5437</td>
      <td>0.0000</td>
      <td>6227.0</td>
      <td>NaN</td>
      <td>206.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 1986 columns</p>
</div>



## Question 6


```python
df.shape
```




    (7112, 1986)




```python
len(df.columns)
```




    1986




```python
len(df)
```




    7112




```python
df.columns
```




    Index(['UNITID', 'OPEID', 'OPEID6', 'INSTNM', 'CITY', 'STABBR', 'ZIP',
           'ACCREDAGENCY', 'INSTURL', 'NPCURL',
           ...
           'OMENRUP_PARTTIME_POOLED_SUPP', 'FTFTPCTPELL', 'FTFTPCTFLOAN', 'UG12MN',
           'G12MN', 'SCUGFFN', 'POOLYRS_FTFTAIDPCT', 'FTFTPCTPELL_POOLED_SUPP',
           'FTFTPCTFLOAN_POOLED_SUPP', 'SCUGFFN_POOLED'],
          dtype='object', length=1986)



## Question 7


```python
df2 = df[['UNITID','OPEID','INSTNM', 'CITY', 'STABBR', 'ZIP','ADM_RATE','UGDS','TUITIONFEE_IN','MN_EARN_WNE_P10']]
df2
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100654</td>
      <td>100200</td>
      <td>Alabama A &amp; M University</td>
      <td>Normal</td>
      <td>AL</td>
      <td>35762</td>
      <td>0.9027</td>
      <td>4824.0</td>
      <td>9857.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100663</td>
      <td>105200</td>
      <td>University of Alabama at Birmingham</td>
      <td>Birmingham</td>
      <td>AL</td>
      <td>35294-0110</td>
      <td>0.9181</td>
      <td>12866.0</td>
      <td>8328.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100690</td>
      <td>2503400</td>
      <td>Amridge University</td>
      <td>Montgomery</td>
      <td>AL</td>
      <td>36117-3553</td>
      <td>NaN</td>
      <td>318.0</td>
      <td>6900.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>100706</td>
      <td>105500</td>
      <td>University of Alabama in Huntsville</td>
      <td>Huntsville</td>
      <td>AL</td>
      <td>35899</td>
      <td>0.8123</td>
      <td>6917.0</td>
      <td>10280.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>100724</td>
      <td>100500</td>
      <td>Alabama State University</td>
      <td>Montgomery</td>
      <td>AL</td>
      <td>36104-0271</td>
      <td>0.9787</td>
      <td>4189.0</td>
      <td>11068.0</td>
      <td>NaN</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>7107</th>
      <td>48312404</td>
      <td>108163</td>
      <td>Arizona State University at Yuma</td>
      <td>Yuma</td>
      <td>AZ</td>
      <td>853656900</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7108</th>
      <td>48387801</td>
      <td>4223701</td>
      <td>Bay Area Medical Academy - San Jose Satellite ...</td>
      <td>San Jose</td>
      <td>CA</td>
      <td>95113</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7109</th>
      <td>48400201</td>
      <td>4228101</td>
      <td>High Desert Medical College - Bakerfield</td>
      <td>Bakersfield</td>
      <td>CA</td>
      <td>93301</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7110</th>
      <td>48778201</td>
      <td>4221501</td>
      <td>BCI - Malden</td>
      <td>Malden</td>
      <td>MA</td>
      <td>021480000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7111</th>
      <td>49005401</td>
      <td>4182601</td>
      <td>HCI College - Fort Lauderdale Campus</td>
      <td>Fort Lauderdale</td>
      <td>FL</td>
      <td>33309</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>22575.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>7112 rows × 10 columns</p>
</div>



## Question 9

UNITID - IPEDS Identification
INSTNM - Institution Name
CITY - Institutions city
STABBR - Institutions state
ZIP -Institutions zip code
ADM_RATE - Admission Rate at each campus
UGDS - Number of degree/certificate-seeking undergraduates enrolled in the fall
TUITIONFEE_IN - In-state students
MN_EARN_WNE_P10 - Mean earnings for the institutional aggregate of all federally aided students

## Question 10a


```python
df2.head(10)
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100654</td>
      <td>100200</td>
      <td>Alabama A &amp; M University</td>
      <td>Normal</td>
      <td>AL</td>
      <td>35762</td>
      <td>0.9027</td>
      <td>4824.0</td>
      <td>9857.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100663</td>
      <td>105200</td>
      <td>University of Alabama at Birmingham</td>
      <td>Birmingham</td>
      <td>AL</td>
      <td>35294-0110</td>
      <td>0.9181</td>
      <td>12866.0</td>
      <td>8328.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100690</td>
      <td>2503400</td>
      <td>Amridge University</td>
      <td>Montgomery</td>
      <td>AL</td>
      <td>36117-3553</td>
      <td>NaN</td>
      <td>318.0</td>
      <td>6900.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>100706</td>
      <td>105500</td>
      <td>University of Alabama in Huntsville</td>
      <td>Huntsville</td>
      <td>AL</td>
      <td>35899</td>
      <td>0.8123</td>
      <td>6917.0</td>
      <td>10280.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>100724</td>
      <td>100500</td>
      <td>Alabama State University</td>
      <td>Montgomery</td>
      <td>AL</td>
      <td>36104-0271</td>
      <td>0.9787</td>
      <td>4189.0</td>
      <td>11068.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>100751</td>
      <td>105100</td>
      <td>The University of Alabama</td>
      <td>Tuscaloosa</td>
      <td>AL</td>
      <td>35487-0100</td>
      <td>0.5330</td>
      <td>32387.0</td>
      <td>10780.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>100760</td>
      <td>100700</td>
      <td>Central Alabama Community College</td>
      <td>Alexander City</td>
      <td>AL</td>
      <td>35010</td>
      <td>NaN</td>
      <td>1404.0</td>
      <td>4440.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100812</td>
      <td>100800</td>
      <td>Athens State University</td>
      <td>Athens</td>
      <td>AL</td>
      <td>35611</td>
      <td>NaN</td>
      <td>2801.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>100830</td>
      <td>831000</td>
      <td>Auburn University at Montgomery</td>
      <td>Montgomery</td>
      <td>AL</td>
      <td>36117-3596</td>
      <td>0.8240</td>
      <td>4211.0</td>
      <td>8020.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>100858</td>
      <td>100900</td>
      <td>Auburn University</td>
      <td>Auburn</td>
      <td>AL</td>
      <td>36849</td>
      <td>0.8393</td>
      <td>23391.0</td>
      <td>10968.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Question 10b


```python
df2.tail(10)
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7102</th>
      <td>48154401</td>
      <td>4220901</td>
      <td>National Personal Training Institute of Cleveland</td>
      <td>Highland Heights</td>
      <td>OH</td>
      <td>44143</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7103</th>
      <td>48305401</td>
      <td>4224601</td>
      <td>Barber School of Pittsburgh - Ambridge</td>
      <td>Ambridge</td>
      <td>PA</td>
      <td>150030000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7104</th>
      <td>48312401</td>
      <td>108131</td>
      <td>Arizona State University at Tucson</td>
      <td>Tucson</td>
      <td>AZ</td>
      <td>857454284</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7105</th>
      <td>48312402</td>
      <td>108161</td>
      <td>Arizona State University - ASU Colleges at Lak...</td>
      <td>Lake Havasu City</td>
      <td>AZ</td>
      <td>864036877</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6904.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7106</th>
      <td>48312403</td>
      <td>108162</td>
      <td>Arizona State University at The Gila Valley</td>
      <td>Thatcher</td>
      <td>AZ</td>
      <td>855525545</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7107</th>
      <td>48312404</td>
      <td>108163</td>
      <td>Arizona State University at Yuma</td>
      <td>Yuma</td>
      <td>AZ</td>
      <td>853656900</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7108</th>
      <td>48387801</td>
      <td>4223701</td>
      <td>Bay Area Medical Academy - San Jose Satellite ...</td>
      <td>San Jose</td>
      <td>CA</td>
      <td>95113</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7109</th>
      <td>48400201</td>
      <td>4228101</td>
      <td>High Desert Medical College - Bakerfield</td>
      <td>Bakersfield</td>
      <td>CA</td>
      <td>93301</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7110</th>
      <td>48778201</td>
      <td>4221501</td>
      <td>BCI - Malden</td>
      <td>Malden</td>
      <td>MA</td>
      <td>021480000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7111</th>
      <td>49005401</td>
      <td>4182601</td>
      <td>HCI College - Fort Lauderdale Campus</td>
      <td>Fort Lauderdale</td>
      <td>FL</td>
      <td>33309</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>22575.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Question 10c


```python
df2.sample(10)
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>331</th>
      <td>115861</td>
      <td>121400</td>
      <td>Imperial Valley College</td>
      <td>Imperial</td>
      <td>CA</td>
      <td>92251-0158</td>
      <td>NaN</td>
      <td>7360.0</td>
      <td>1142.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4224</th>
      <td>373711</td>
      <td>466900</td>
      <td>Upper Cape Cod Regional Technical School</td>
      <td>Bourne</td>
      <td>MA</td>
      <td>02532</td>
      <td>0.6897</td>
      <td>87.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2804</th>
      <td>206437</td>
      <td>313500</td>
      <td>Walsh University</td>
      <td>North Canton</td>
      <td>OH</td>
      <td>44720-3396</td>
      <td>0.7923</td>
      <td>1929.0</td>
      <td>29150.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2034</th>
      <td>182634</td>
      <td>257200</td>
      <td>Colby-Sawyer College</td>
      <td>New London</td>
      <td>NH</td>
      <td>03257-7835</td>
      <td>0.8727</td>
      <td>963.0</td>
      <td>41186.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3834</th>
      <td>238397</td>
      <td>539000</td>
      <td>Blackhawk Technical College</td>
      <td>Janesville</td>
      <td>WI</td>
      <td>53547-5009</td>
      <td>NaN</td>
      <td>2098.0</td>
      <td>4329.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6079</th>
      <td>480107</td>
      <td>3010633</td>
      <td>Virginia College-Florence</td>
      <td>Florence</td>
      <td>SC</td>
      <td>29501</td>
      <td>NaN</td>
      <td>345.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1622</th>
      <td>168227</td>
      <td>222500</td>
      <td>Wentworth Institute of Technology</td>
      <td>Boston</td>
      <td>MA</td>
      <td>02115</td>
      <td>0.9187</td>
      <td>4204.0</td>
      <td>34977.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4039</th>
      <td>248624</td>
      <td>533000</td>
      <td>Fayette County Career &amp; Technical Institute Pr...</td>
      <td>Uniontown</td>
      <td>PA</td>
      <td>15401</td>
      <td>NaN</td>
      <td>90.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3322</th>
      <td>220215</td>
      <td>349200</td>
      <td>Freed-Hardeman University</td>
      <td>Henderson</td>
      <td>TN</td>
      <td>38340-2399</td>
      <td>0.9532</td>
      <td>1319.0</td>
      <td>21950.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1110</th>
      <td>151333</td>
      <td>181400</td>
      <td>Indiana University-Kokomo</td>
      <td>Kokomo</td>
      <td>IN</td>
      <td>46902-9003</td>
      <td>0.7028</td>
      <td>2746.0</td>
      <td>7207.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.describe()
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>7.112000e+03</td>
      <td>7.112000e+03</td>
      <td>2037.000000</td>
      <td>6364.000000</td>
      <td>4021.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.867121e+06</td>
      <td>1.866750e+06</td>
      <td>0.682206</td>
      <td>2427.972659</td>
      <td>15097.328277</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>6.958737e+06</td>
      <td>3.315240e+06</td>
      <td>0.212439</td>
      <td>5485.131878</td>
      <td>12725.207303</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.006540e+05</td>
      <td>1.002000e+05</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>480.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.740728e+05</td>
      <td>3.229750e+05</td>
      <td>0.550800</td>
      <td>106.000000</td>
      <td>5252.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2.289995e+05</td>
      <td>1.056050e+06</td>
      <td>0.707700</td>
      <td>401.000000</td>
      <td>11330.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>4.506005e+05</td>
      <td>3.025825e+06</td>
      <td>0.838600</td>
      <td>2011.250000</td>
      <td>19400.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>4.900540e+07</td>
      <td>8.209884e+07</td>
      <td>1.000000</td>
      <td>77269.000000</td>
      <td>74514.000000</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfmd = df2[df2.STABBR == 'MD']
dfmd
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1446</th>
      <td>161651</td>
      <td>3097200</td>
      <td>Aesthetics Institute of Cosmetology</td>
      <td>Gaithersburg</td>
      <td>MD</td>
      <td>20877</td>
      <td>NaN</td>
      <td>25.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>161688</td>
      <td>205700</td>
      <td>Allegany College of Maryland</td>
      <td>Cumberland</td>
      <td>MD</td>
      <td>21502-2596</td>
      <td>NaN</td>
      <td>1990.0</td>
      <td>3940.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>161767</td>
      <td>205800</td>
      <td>Anne Arundel Community College</td>
      <td>Arnold</td>
      <td>MD</td>
      <td>21012-1895</td>
      <td>NaN</td>
      <td>11294.0</td>
      <td>4646.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>161776</td>
      <td>1041000</td>
      <td>Brightwood College-Towson</td>
      <td>Towson</td>
      <td>MD</td>
      <td>21286-2201</td>
      <td>NaN</td>
      <td>309.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>161800</td>
      <td>826300</td>
      <td>Award Beauty School</td>
      <td>Hagerstown</td>
      <td>MD</td>
      <td>21740-5610</td>
      <td>NaN</td>
      <td>157.0</td>
      <td>NaN</td>
      <td>NaN</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>6800</th>
      <td>16210401</td>
      <td>830801</td>
      <td>Cecil College - Elkton Station</td>
      <td>Elkton</td>
      <td>MD</td>
      <td>219215535</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4005.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7004</th>
      <td>43018401</td>
      <td>145919</td>
      <td>Strayer University-Rockville Campus</td>
      <td>Rockville</td>
      <td>MD</td>
      <td>20850</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>13857.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7005</th>
      <td>43018402</td>
      <td>145923</td>
      <td>Strayer University-Anne Arundel Campus</td>
      <td>Millersville</td>
      <td>MD</td>
      <td>21108</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>13857.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7006</th>
      <td>43018403</td>
      <td>145924</td>
      <td>Strayer University-White Marsh Campus</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21236</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>13857.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7007</th>
      <td>43018404</td>
      <td>145926</td>
      <td>Strayer University-Owings Mills Campus</td>
      <td>Owings Mills</td>
      <td>MD</td>
      <td>21117</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>13857.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>91 rows × 10 columns</p>
</div>




```python
dfbalt = dfmd[dfmd.CITY == 'Baltimore']
dfbalt
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1451</th>
      <td>161855</td>
      <td>2494700</td>
      <td>Baltimore Studio of Hair Design</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21201-3444</td>
      <td>NaN</td>
      <td>46.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>161864</td>
      <td>206100</td>
      <td>Baltimore City Community College</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21215-7893</td>
      <td>NaN</td>
      <td>3797.0</td>
      <td>3074.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>161873</td>
      <td>210200</td>
      <td>University of Baltimore</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21201-5720</td>
      <td>0.8099</td>
      <td>2856.0</td>
      <td>8824.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1460</th>
      <td>162283</td>
      <td>206800</td>
      <td>Coppin State University</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21216-3698</td>
      <td>0.3651</td>
      <td>2459.0</td>
      <td>7474.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1462</th>
      <td>162371</td>
      <td>2545400</td>
      <td>North American Trade Schools</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21244</td>
      <td>NaN</td>
      <td>448.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1466</th>
      <td>162654</td>
      <td>207300</td>
      <td>Goucher College</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21204-2794</td>
      <td>0.7884</td>
      <td>1526.0</td>
      <td>43440.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1473</th>
      <td>162928</td>
      <td>207700</td>
      <td>Johns Hopkins University</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21218-2688</td>
      <td>0.1254</td>
      <td>5663.0</td>
      <td>52170.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1475</th>
      <td>163046</td>
      <td>207800</td>
      <td>Loyola University Maryland</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21210-2699</td>
      <td>0.7528</td>
      <td>3903.0</td>
      <td>47560.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1477</th>
      <td>163259</td>
      <td>210400</td>
      <td>University of Maryland Baltimore</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21201-1627</td>
      <td>NaN</td>
      <td>918.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1478</th>
      <td>163268</td>
      <td>210500</td>
      <td>University of Maryland-Baltimore County</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21250</td>
      <td>0.6021</td>
      <td>11130.0</td>
      <td>11518.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1480</th>
      <td>163295</td>
      <td>208000</td>
      <td>Maryland Institute College of Art</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21217-4134</td>
      <td>0.6161</td>
      <td>1743.0</td>
      <td>46990.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1485</th>
      <td>163453</td>
      <td>208300</td>
      <td>Morgan State University</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21251-0001</td>
      <td>0.6372</td>
      <td>6426.0</td>
      <td>7766.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1487</th>
      <td>163532</td>
      <td>208700</td>
      <td>Ner Israel Rabbinical College</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21208</td>
      <td>0.6418</td>
      <td>265.0</td>
      <td>11900.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1489</th>
      <td>163578</td>
      <td>206500</td>
      <td>Notre Dame of Maryland University</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21210-2476</td>
      <td>0.7140</td>
      <td>808.0</td>
      <td>36070.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1491</th>
      <td>163736</td>
      <td>749100</td>
      <td>Brightwood College-Baltimore</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21227-1063</td>
      <td>NaN</td>
      <td>452.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1493</th>
      <td>163815</td>
      <td>2331000</td>
      <td>Maryland Beauty Academy of Essex</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21224</td>
      <td>NaN</td>
      <td>80.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3004</th>
      <td>212452</td>
      <td>3667300</td>
      <td>Faith Theological Seminary</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21212-2624</td>
      <td>1.0000</td>
      <td>66.0</td>
      <td>5870.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4225</th>
      <td>373784</td>
      <td>3493300</td>
      <td>All-State Career-Baltimore</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21224</td>
      <td>NaN</td>
      <td>561.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4762</th>
      <td>434672</td>
      <td>206300</td>
      <td>Community College of Baltimore County</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21237</td>
      <td>NaN</td>
      <td>17614.0</td>
      <td>4022.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5314</th>
      <td>450076</td>
      <td>3493301</td>
      <td>Fortis Institute-Baltimore</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21244</td>
      <td>NaN</td>
      <td>87.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5834</th>
      <td>461379</td>
      <td>4168900</td>
      <td>Holistic Massage Training Institute</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21218</td>
      <td>NaN</td>
      <td>59.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6016</th>
      <td>476601</td>
      <td>4188400</td>
      <td>Bais HaMedrash and Mesivta of Baltimore</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21209-1613</td>
      <td>1.0000</td>
      <td>76.0</td>
      <td>12700.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7006</th>
      <td>43018403</td>
      <td>145924</td>
      <td>Strayer University-White Marsh Campus</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21236</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>13857.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfcp = dfmd[dfmd.CITY == 'College Park']
dfcp
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1479</th>
      <td>163286</td>
      <td>210300</td>
      <td>University of Maryland-College Park</td>
      <td>College Park</td>
      <td>MD</td>
      <td>20742</td>
      <td>0.445</td>
      <td>29273.0</td>
      <td>10399.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfjh = dfbalt[dfbalt.INSTNM == 'Johns Hopkins University']
dfjh
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1473</th>
      <td>162928</td>
      <td>207700</td>
      <td>Johns Hopkins University</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21218-2688</td>
      <td>0.1254</td>
      <td>5663.0</td>
      <td>52170.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfumbc = dfbalt[dfbalt.INSTNM == 'University of Maryland-Baltimore County']
dfumbc
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1478</th>
      <td>163268</td>
      <td>210500</td>
      <td>University of Maryland-Baltimore County</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21250</td>
      <td>0.6021</td>
      <td>11130.0</td>
      <td>11518.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfl = dfbalt[dfbalt.INSTNM == 'Loyola University Maryland']
dfl
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1475</th>
      <td>163046</td>
      <td>207800</td>
      <td>Loyola University Maryland</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21210-2699</td>
      <td>0.7528</td>
      <td>3903.0</td>
      <td>47560.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Question 10d-g


```python
display(dfl)
display(dfjh)
display(dfcp)
display(dfumbc)
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1475</th>
      <td>163046</td>
      <td>207800</td>
      <td>Loyola University Maryland</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21210-2699</td>
      <td>0.7528</td>
      <td>3903.0</td>
      <td>47560.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1473</th>
      <td>162928</td>
      <td>207700</td>
      <td>Johns Hopkins University</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21218-2688</td>
      <td>0.1254</td>
      <td>5663.0</td>
      <td>52170.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1479</th>
      <td>163286</td>
      <td>210300</td>
      <td>University of Maryland-College Park</td>
      <td>College Park</td>
      <td>MD</td>
      <td>20742</td>
      <td>0.445</td>
      <td>29273.0</td>
      <td>10399.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1478</th>
      <td>163268</td>
      <td>210500</td>
      <td>University of Maryland-Baltimore County</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21250</td>
      <td>0.6021</td>
      <td>11130.0</td>
      <td>11518.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



```python
dfm4 = pd.concat([dfl,dfjh,dfcp,dfumbc], ignore_index = True)
dfm4
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>163046</td>
      <td>207800</td>
      <td>Loyola University Maryland</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21210-2699</td>
      <td>0.7528</td>
      <td>3903.0</td>
      <td>47560.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>162928</td>
      <td>207700</td>
      <td>Johns Hopkins University</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21218-2688</td>
      <td>0.1254</td>
      <td>5663.0</td>
      <td>52170.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>163286</td>
      <td>210300</td>
      <td>University of Maryland-College Park</td>
      <td>College Park</td>
      <td>MD</td>
      <td>20742</td>
      <td>0.4450</td>
      <td>29273.0</td>
      <td>10399.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>163268</td>
      <td>210500</td>
      <td>University of Maryland-Baltimore County</td>
      <td>Baltimore</td>
      <td>MD</td>
      <td>21250</td>
      <td>0.6021</td>
      <td>11130.0</td>
      <td>11518.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfm4['TUITIONFEE_IN'].min()

```




    10399.0




```python
dfm4['TUITIONFEE_IN'].max()
```




    52170.0



## Question 10h


```python
dfm4['TUITIONFEE_IN'].describe()
```




    count        4.000000
    mean     30411.750000
    std      22546.011271
    min      10399.000000
    25%      11238.250000
    50%      29539.000000
    75%      48712.500000
    max      52170.000000
    Name: TUITIONFEE_IN, dtype: float64




```python
dfva = df2[df2.STABBR == 'VA']
dfva
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3627</th>
      <td>231280</td>
      <td>3010700</td>
      <td>Paul Mitchell the School-Roanoke</td>
      <td>Roanoke</td>
      <td>VA</td>
      <td>24015</td>
      <td>NaN</td>
      <td>84.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3628</th>
      <td>231411</td>
      <td>3127500</td>
      <td>Advanced Technology Institute</td>
      <td>Virginia Beach</td>
      <td>VA</td>
      <td>23462</td>
      <td>0.7954</td>
      <td>464.0</td>
      <td>13250.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3629</th>
      <td>231420</td>
      <td>370200</td>
      <td>Averett University</td>
      <td>Danville</td>
      <td>VA</td>
      <td>24541</td>
      <td>0.6102</td>
      <td>908.0</td>
      <td>33350.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3630</th>
      <td>231536</td>
      <td>681900</td>
      <td>Blue Ridge Community College</td>
      <td>Weyers Cave</td>
      <td>VA</td>
      <td>24486-0080</td>
      <td>NaN</td>
      <td>3054.0</td>
      <td>5252.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3631</th>
      <td>231554</td>
      <td>370300</td>
      <td>Bluefield College</td>
      <td>Bluefield</td>
      <td>VA</td>
      <td>24605</td>
      <td>0.9112</td>
      <td>874.0</td>
      <td>24800.0</td>
      <td>NaN</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>6969</th>
      <td>24893411</td>
      <td>1019814</td>
      <td>ECPI University-Virginia Beach Health Sciences</td>
      <td>Virginia Beach</td>
      <td>VA</td>
      <td>234621603</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15261.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6970</th>
      <td>24893412</td>
      <td>1019815</td>
      <td>ECPI University-Richmond South</td>
      <td>Richmond</td>
      <td>VA</td>
      <td>232361603</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>14985.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6971</th>
      <td>24893413</td>
      <td>1019816</td>
      <td>ECPI University-Innsbrook</td>
      <td>Glen Allen</td>
      <td>VA</td>
      <td>230601603</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15263.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6972</th>
      <td>24893414</td>
      <td>1019817</td>
      <td>ECPI University-Richmond West</td>
      <td>Richmond</td>
      <td>VA</td>
      <td>232941603</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>16039.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6973</th>
      <td>24893415</td>
      <td>1019818</td>
      <td>ECPI University - Roanoke</td>
      <td>Roanoke</td>
      <td>VA</td>
      <td>240121603</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15525.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>177 rows × 10 columns</p>
</div>




```python
dfpa = df2[df2.STABBR == 'PA']
dfpa
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2933</th>
      <td>210474</td>
      <td>2178900</td>
      <td>Jolie Hair and Beauty Academy-Hazleton</td>
      <td>Hazleton</td>
      <td>PA</td>
      <td>18201</td>
      <td>NaN</td>
      <td>61.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2934</th>
      <td>210492</td>
      <td>322800</td>
      <td>Bryn Athyn College of the New Church</td>
      <td>Bryn Athyn</td>
      <td>PA</td>
      <td>19009-0711</td>
      <td>0.8755</td>
      <td>323.0</td>
      <td>21126.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2935</th>
      <td>210508</td>
      <td>3353300</td>
      <td>Academy of Vocal Arts</td>
      <td>Philadelphia</td>
      <td>PA</td>
      <td>19103-6685</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2936</th>
      <td>210571</td>
      <td>322900</td>
      <td>Albright College</td>
      <td>Reading</td>
      <td>PA</td>
      <td>19612-5234</td>
      <td>0.5004</td>
      <td>1999.0</td>
      <td>43454.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2937</th>
      <td>210599</td>
      <td>2495500</td>
      <td>All-State Career School</td>
      <td>Essington</td>
      <td>PA</td>
      <td>19029</td>
      <td>NaN</td>
      <td>306.0</td>
      <td>NaN</td>
      <td>NaN</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>7023</th>
      <td>44378405</td>
      <td>145950</td>
      <td>Strayer University-Warrendale Campus</td>
      <td>Warrendale</td>
      <td>PA</td>
      <td>15086</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>13857.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7024</th>
      <td>44378406</td>
      <td>145976</td>
      <td>Strayer University-Allentown Campus</td>
      <td>Center Valley</td>
      <td>PA</td>
      <td>18034</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>13857.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7063</th>
      <td>45794301</td>
      <td>4149801</td>
      <td>Somerset County Technology Center - Bedford Site</td>
      <td>Bedford</td>
      <td>PA</td>
      <td>15522</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7089</th>
      <td>47503308</td>
      <td>4208608</td>
      <td>Relay Graduate School of Education - Philadelp...</td>
      <td>Philadelphia</td>
      <td>PA</td>
      <td>191224906</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7103</th>
      <td>48305401</td>
      <td>4224601</td>
      <td>Barber School of Pittsburgh - Ambridge</td>
      <td>Ambridge</td>
      <td>PA</td>
      <td>150030000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>378 rows × 10 columns</p>
</div>




```python
dfdc = df2[df2.STABBR == 'DC']
dfdc
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>643</th>
      <td>131159</td>
      <td>143400</td>
      <td>American University</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20016-8001</td>
      <td>0.2940</td>
      <td>7433.0</td>
      <td>46615.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>644</th>
      <td>131283</td>
      <td>143700</td>
      <td>The Catholic University of America</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20064</td>
      <td>0.8258</td>
      <td>3284.0</td>
      <td>44060.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>645</th>
      <td>131399</td>
      <td>144100</td>
      <td>University of the District of Columbia</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20008</td>
      <td>NaN</td>
      <td>3606.0</td>
      <td>5756.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>646</th>
      <td>131405</td>
      <td>1280300</td>
      <td>Pontifical Faculty of the Immaculate Conceptio...</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20017-1585</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>647</th>
      <td>131450</td>
      <td>144300</td>
      <td>Gallaudet University</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20002-3695</td>
      <td>0.5901</td>
      <td>1111.0</td>
      <td>16558.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>648</th>
      <td>131469</td>
      <td>144400</td>
      <td>George Washington University</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20052</td>
      <td>0.4098</td>
      <td>11718.0</td>
      <td>53518.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>649</th>
      <td>131496</td>
      <td>144500</td>
      <td>Georgetown University</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20057-0001</td>
      <td>0.1568</td>
      <td>7128.0</td>
      <td>52300.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>650</th>
      <td>131520</td>
      <td>144800</td>
      <td>Howard University</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20059-0001</td>
      <td>0.4142</td>
      <td>6276.0</td>
      <td>25697.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>651</th>
      <td>131803</td>
      <td>145900</td>
      <td>Strayer University-District of Columbia</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20005</td>
      <td>NaN</td>
      <td>687.0</td>
      <td>13857.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>652</th>
      <td>131830</td>
      <td>2132800</td>
      <td>National Conservatory of Dramatic Arts</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20007</td>
      <td>1.0000</td>
      <td>32.0</td>
      <td>9900.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>653</th>
      <td>131876</td>
      <td>146000</td>
      <td>Trinity Washington University</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20017-1094</td>
      <td>0.9228</td>
      <td>1498.0</td>
      <td>23690.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>654</th>
      <td>131973</td>
      <td>146400</td>
      <td>Wesley Theological Seminary</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20016-5690</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4100</th>
      <td>363721</td>
      <td>144102</td>
      <td>University of the District of Columbia-David A...</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20008</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4348</th>
      <td>384412</td>
      <td>3218300</td>
      <td>University of the Potomac-Washington DC Campus</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20005</td>
      <td>NaN</td>
      <td>65.0</td>
      <td>13884.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4616</th>
      <td>420370</td>
      <td>3104300</td>
      <td>Career Technical Institute</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20005</td>
      <td>NaN</td>
      <td>387.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4844</th>
      <td>439473</td>
      <td>3409600</td>
      <td>Bennett Career Institute</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20017</td>
      <td>NaN</td>
      <td>312.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5079</th>
      <td>444893</td>
      <td>3750300</td>
      <td>Technical Learning Centers Inc</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20006-5540</td>
      <td>NaN</td>
      <td>172.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5328</th>
      <td>450483</td>
      <td>32098812</td>
      <td>University of Phoenix-Washington DC</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20001-1431</td>
      <td>NaN</td>
      <td>70.0</td>
      <td>9960.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5520</th>
      <td>455804</td>
      <td>4114400</td>
      <td>Institute of World Politics</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20036</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5521</th>
      <td>455813</td>
      <td>4142700</td>
      <td>Pontifical John Paul II Institute for Studies ...</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20064</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5739</th>
      <td>459745</td>
      <td>2155306</td>
      <td>The Chicago School of Professional Psychology ...</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20005</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5747</th>
      <td>459994</td>
      <td>145900</td>
      <td>Strayer University-Global Region</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20005</td>
      <td>NaN</td>
      <td>5543.0</td>
      <td>13857.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6727</th>
      <td>13180301</td>
      <td>145904</td>
      <td>Strayer University-Takoma Park Campus</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20012</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>13857.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7094</th>
      <td>47503313</td>
      <td>4208613</td>
      <td>Relay Graduate School of Education - Washingto...</td>
      <td>Washington</td>
      <td>DC</td>
      <td>20002</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfde = df2[df2.STABBR == 'DE']
dfde
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>634</th>
      <td>130837</td>
      <td>2125200</td>
      <td>Margaret H Rollins School of Nursing at Beebe ...</td>
      <td>Lewes</td>
      <td>DE</td>
      <td>19958</td>
      <td>NaN</td>
      <td>59.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>635</th>
      <td>130873</td>
      <td>3025800</td>
      <td>Dawn Career Institute LLC</td>
      <td>Newark</td>
      <td>DE</td>
      <td>19702</td>
      <td>NaN</td>
      <td>108.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>636</th>
      <td>130907</td>
      <td>1172700</td>
      <td>Delaware Technical Community College-Terry</td>
      <td>Dover</td>
      <td>DE</td>
      <td>19901</td>
      <td>NaN</td>
      <td>12408.0</td>
      <td>4848.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>637</th>
      <td>130934</td>
      <td>142800</td>
      <td>Delaware State University</td>
      <td>Dover</td>
      <td>DE</td>
      <td>19901</td>
      <td>0.4518</td>
      <td>3678.0</td>
      <td>7868.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>638</th>
      <td>130943</td>
      <td>143100</td>
      <td>University of Delaware</td>
      <td>Newark</td>
      <td>DE</td>
      <td>19716</td>
      <td>0.6289</td>
      <td>18948.0</td>
      <td>13160.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>639</th>
      <td>130989</td>
      <td>142900</td>
      <td>Goldey-Beacom College</td>
      <td>Wilmington</td>
      <td>DE</td>
      <td>19808</td>
      <td>0.5177</td>
      <td>770.0</td>
      <td>23850.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>640</th>
      <td>131061</td>
      <td>2190400</td>
      <td>Schilling-Douglas School of Hair Design LLC</td>
      <td>Newark</td>
      <td>DE</td>
      <td>19711</td>
      <td>NaN</td>
      <td>133.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>641</th>
      <td>131098</td>
      <td>143300</td>
      <td>Wesley College</td>
      <td>Dover</td>
      <td>DE</td>
      <td>19901-3875</td>
      <td>0.6151</td>
      <td>1342.0</td>
      <td>26406.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>642</th>
      <td>131113</td>
      <td>794800</td>
      <td>Wilmington University</td>
      <td>New Castle</td>
      <td>DE</td>
      <td>19720</td>
      <td>NaN</td>
      <td>8346.0</td>
      <td>10940.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4729</th>
      <td>432524</td>
      <td>4139800</td>
      <td>Delaware College of Art and Design</td>
      <td>Wilmington</td>
      <td>DE</td>
      <td>19801-3007</td>
      <td>0.7900</td>
      <td>143.0</td>
      <td>25710.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4917</th>
      <td>441362</td>
      <td>3543300</td>
      <td>Harris School of Business-Wilmington Campus</td>
      <td>Wilmington</td>
      <td>DE</td>
      <td>19803</td>
      <td>NaN</td>
      <td>219.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5037</th>
      <td>444200</td>
      <td>2586902</td>
      <td>Harris School of Business-Dover Campus</td>
      <td>Dover</td>
      <td>DE</td>
      <td>19901</td>
      <td>NaN</td>
      <td>226.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5275</th>
      <td>449472</td>
      <td>3702300</td>
      <td>Delaware Learning Institute of Cosmetology</td>
      <td>Dagsboro</td>
      <td>DE</td>
      <td>19939</td>
      <td>NaN</td>
      <td>39.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5322</th>
      <td>450298</td>
      <td>145948</td>
      <td>Strayer University-Delaware</td>
      <td>Newark</td>
      <td>DE</td>
      <td>19713</td>
      <td>NaN</td>
      <td>267.0</td>
      <td>13857.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5354</th>
      <td>451051</td>
      <td>4130700</td>
      <td>Academy of Massage and Bodywork</td>
      <td>Bear</td>
      <td>DE</td>
      <td>19701</td>
      <td>NaN</td>
      <td>95.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5718</th>
      <td>459301</td>
      <td>4171100</td>
      <td>Paul Mitchell the School-Delaware</td>
      <td>Newark</td>
      <td>DE</td>
      <td>19702</td>
      <td>NaN</td>
      <td>103.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6527</th>
      <td>488262</td>
      <td>4250300</td>
      <td>Hair Academy School of Barbering &amp; Beauty</td>
      <td>Newark</td>
      <td>DE</td>
      <td>19713-2305</td>
      <td>NaN</td>
      <td>33.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6725</th>
      <td>13090701</td>
      <td>1172702</td>
      <td>Delaware Technical Community College-Owens</td>
      <td>Georgetown</td>
      <td>DE</td>
      <td>19947</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4848.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6726</th>
      <td>13090702</td>
      <td>1172703</td>
      <td>Delaware Technical Community College-Stanton/W...</td>
      <td>Wilmington</td>
      <td>DE</td>
      <td>19801</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4848.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7084</th>
      <td>47503303</td>
      <td>4208605</td>
      <td>Relay Graduate School of Education - Delaware</td>
      <td>Wilmington</td>
      <td>DE</td>
      <td>19801</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



# Question - 11 Combining 5 states


```python
fvstatecol = pd.concat([dfde,dfpa,dfmd,dfva], ignore_index = True)
fvstatecol
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
      <th>UNITID</th>
      <th>OPEID</th>
      <th>INSTNM</th>
      <th>CITY</th>
      <th>STABBR</th>
      <th>ZIP</th>
      <th>ADM_RATE</th>
      <th>UGDS</th>
      <th>TUITIONFEE_IN</th>
      <th>MN_EARN_WNE_P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>130837</td>
      <td>2125200</td>
      <td>Margaret H Rollins School of Nursing at Beebe ...</td>
      <td>Lewes</td>
      <td>DE</td>
      <td>19958</td>
      <td>NaN</td>
      <td>59.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>130873</td>
      <td>3025800</td>
      <td>Dawn Career Institute LLC</td>
      <td>Newark</td>
      <td>DE</td>
      <td>19702</td>
      <td>NaN</td>
      <td>108.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>130907</td>
      <td>1172700</td>
      <td>Delaware Technical Community College-Terry</td>
      <td>Dover</td>
      <td>DE</td>
      <td>19901</td>
      <td>NaN</td>
      <td>12408.0</td>
      <td>4848.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>130934</td>
      <td>142800</td>
      <td>Delaware State University</td>
      <td>Dover</td>
      <td>DE</td>
      <td>19901</td>
      <td>0.4518</td>
      <td>3678.0</td>
      <td>7868.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>130943</td>
      <td>143100</td>
      <td>University of Delaware</td>
      <td>Newark</td>
      <td>DE</td>
      <td>19716</td>
      <td>0.6289</td>
      <td>18948.0</td>
      <td>13160.0</td>
      <td>NaN</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>661</th>
      <td>24893411</td>
      <td>1019814</td>
      <td>ECPI University-Virginia Beach Health Sciences</td>
      <td>Virginia Beach</td>
      <td>VA</td>
      <td>234621603</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15261.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>662</th>
      <td>24893412</td>
      <td>1019815</td>
      <td>ECPI University-Richmond South</td>
      <td>Richmond</td>
      <td>VA</td>
      <td>232361603</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>14985.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>663</th>
      <td>24893413</td>
      <td>1019816</td>
      <td>ECPI University-Innsbrook</td>
      <td>Glen Allen</td>
      <td>VA</td>
      <td>230601603</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15263.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>664</th>
      <td>24893414</td>
      <td>1019817</td>
      <td>ECPI University-Richmond West</td>
      <td>Richmond</td>
      <td>VA</td>
      <td>232941603</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>16039.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>665</th>
      <td>24893415</td>
      <td>1019818</td>
      <td>ECPI University - Roanoke</td>
      <td>Roanoke</td>
      <td>VA</td>
      <td>240121603</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>15525.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>666 rows × 10 columns</p>
</div>



# Question 11 - Create CSV file with new DF


```python
fvstatecol.to_csv(r'C:\Users\sheka\Desktop\UMBC\690\Five_States_Colleges.csv', index = False)
```


```python

```
