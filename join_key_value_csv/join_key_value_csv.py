# coding: utf-8


import pandas as pd

keys = pd.read_csv("keys.csv")
values = pd.read_csv("values.csv")


print(keys)


print(values)


kList = list(keys.values.flatten())*10
len(kList)


vList = list(values.values.flatten())[0:100]
len(vList)


pd.DataFrame(
    {'kyes':kList,
     'values':vList
             })


df = pd.DataFrame(
    {'kyes':kList,
     'values':vList
             })
df.to_csv("dammy.csv", index=False)

