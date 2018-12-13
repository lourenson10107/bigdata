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

```python
import pandas as pd
import numpy as np
```


```python
state_fruit.stack()
```


**hasil yang menjadi output**

    Texas    Apple      12
             Orange     10
             Banana     40
    Arizona  Apple       9
             Orange      7
             Banana     12
    Florida  Apple       0
             Orange     14
             Banana    190
    dtype: int64




```python

```



```python
import pandas as pd
import numpy as np
```


```python
state_fruit_tidy = state_fruit.stack().reset_index()
state_fruit_tidy
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
**hasil yang menjadi output**

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>level_0</th>
      <th>level_1</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Texas</td>
      <td>Apple</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Texas</td>
      <td>Orange</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Texas</td>
      <td>Banana</td>
      <td>40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arizona</td>
      <td>Apple</td>
      <td>9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Arizona</td>
      <td>Orange</td>
      <td>7</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Arizona</td>
      <td>Banana</td>
      <td>12</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Florida</td>
      <td>Apple</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Florida</td>
      <td>Orange</td>
      <td>14</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Florida</td>
      <td>Banana</td>
      <td>190</td>
    </tr>
  </tbody>
</table>
</div>




```python

```















