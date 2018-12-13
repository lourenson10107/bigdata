# Pertemuan 13
## Bab 8: Merestrukturisasi Data menjadi Bentuk Tidy

```python
import pandas as pd
import numpy as np
```


```python
state_fruit = pd.read_csv('data/state_fruit.csv', index_col=0)
state_fruit
```


**hasil yang menjadi output**

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
      <th>Apple</th>
      <th>Orange</th>
      <th>Banana</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Texas</th>
      <td>12</td>
      <td>10</td>
      <td>40</td>
    </tr>
    <tr>
      <th>Arizona</th>
      <td>9</td>
      <td>7</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>0</td>
      <td>14</td>
      <td>190</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
