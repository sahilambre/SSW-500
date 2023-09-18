# import pandas as pd
# data = [2,2,3,4,5]
# df = pd.DataFrame(data)
# print (df)
# ----------------------
# import pandas as pd
# data = [['Alex',10],['Bob',12],['Clarke',13]]
# df = pd.DataFrame(data,columns=['Name','Age'])
# print (df)
# ----------------------------
# import pandas as pd
# data = [['Alex',10],['Bob',12],['Clarke',13]]
# df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
# print (df)
# ---------------------------
# import pandas as pd
# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data)
# print (df)
# ----------------------------
# import pandas as pd
# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
# print (df)
# -------------------------
# import pandas as pd
# data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
# df = pd.DataFrame(data)
# print (df)
# ---------------------------
# import pandas as pd
# data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
# df = pd.DataFrame(data, index=['first', 'second'])
# print (df)
# ----------------------------
# import pandas as pd
# data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
# #With two column indices, values same as dictionary keys
# df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
# #With two column indices with one index with other name
# df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
# print (df1)
# print (df2)
# -----------------------------------
# import pandas as pd
# import numpy as np
# unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
# sorted_df = unsorted_df.sort_values(by='col1') # add 'ascending=False' and check
# out the results
# print (sorted_df)
# -------------------------
# indexing and selecting: loc() method
# --------------------------
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(8, 4),\
# index = ['a','b','c','d','e','f','g','h'],\
# columns = ['A', 'B', 'C', 'D'])
# #select all rows for a specific column
# print (df.loc[:,'A'])
# --------------------------
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(8, 4), \
# index = ['a','b','c','d','e','f','g','h'],\
# columns = ['A', 'B', 'C', 'D'])
# # Select all rows for multiple columns
# print (df.loc[:,['A','C']])
# ------------------------------
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(8, 4), \
# index = ['a','b','c','d','e','f','g','h'], \
# columns = ['A', 'B', 'C', 'D'])
# # Select few rows for multiple columns, say list[]
# print (df.loc[['a','b','f','h'],['A','C']])
# ----------------------------
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(8, 4), \
# index = ['a','b','c','d','e','f','g','h'], \
# columns = ['A', 'B', 'C', 'D'])
# # Select range of rows for all columns
# print (df.loc['a':'h'])
# ------------------------------
# indexing and selecting: iloc() method
# ------------------------------
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
# # Integer slicing
# print (df.iloc[:4])
# print (df.iloc[1:5, 2:4])
# ----------------------
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
# # Slicing through list of values
# print (df.iloc[[1, 3, 5], [1, 3]])
# print (df.iloc[1:3, :])
# print (df.iloc[:,1:3])
# -------------------
# import pandas as pd
# import numpy as np
# t = np.arange(0,10,0.1)
# x = np.sin(t)
# y = np.cos(t)
# df = pd.DataFrame({'Time':t, 'x':x, 'y':y})
# print ("Here is my DataFarme --->","\n",df)
# print (df.Time)
# print (df['Time'])
# data = df [['Time','y']]
# print (data)
# print (data [4:10])
# print (df [4:10])
# print (df[['Time','x']][4:10]) # or : print (df[4:10][['Time','x']])
# ------------------------------------
# Grouped bar plots
# --------------------------------------
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
# df.plot.bar()
# ----------------------------
# stacked bar plot
# -------------------------
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
# df.plot.bar(stacked=True)
# -------------------------
# horizontal bar plots
# -----------------------
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
# df.plot.barh(stacked=True)
# -------------------
# practice 1: grouped bar plots
# --------------------
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# df = pd.DataFrame (np.random.randint (20, 150, (8,10)),\
# columns = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j'])
# df.plot.bar ()
# plt.legend (loc=2) # loc =1 the legend will be in the upper right corner
# plt.show()
# ------------------------------
# box plot
# -----------------------------
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
# df.plot.box()
# -----------------------
# scatter plot
# -----------------------
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
# df.plot.scatter(x='a', y='b')
# --------------------
# practice 2: stacked bar plot
# ---------------------
# import matplotlib.pyplot as plt
# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# men_means = [20, 35, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]
# men_std = [2, 3, 4, 1, 2]
# women_std = [3, 5, 2, 3, 3]
# width = 0.35
# fig, ax = plt.subplots()
# ax.bar(labels, men_means, width, yerr=men_std, label='Men')
# ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,label='Women')
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.legend()
# plt.show()