import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})
data.head()

data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value = 0).astype(int)
data.columns = data.columns.droplevel()
data.columns.name = None
data.head()



\\или
\\import pandas as pd
\\import random
\\lst = ['robot'] * 10
\\lst += ['human'] * 10
\\random.shuffle(lst)
\\data = pd.DataFrame({'whoAmI': lst})
\\one_hot_data = pd.DataFrame()
\\for value in data['whoAmI'].unique():
\\    one_hot_data[value] = data['whoAmI'].apply(lambda x: 1 if x == value else 0)
\\print(one_hot_data.head())
