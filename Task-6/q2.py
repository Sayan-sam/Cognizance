# %% [markdown]
# ##### Reading the data set into a list of dictionaries

# %%
from csv import DictReader
import pandas as pd

with open("dataset.csv") as file:
    data = list(DictReader(file))
    

# %% [markdown]
# ##### Finding out all the columns that have the potential nil values.

# %%
list = []
for k in data[0].keys():
    for df in data:
        if(df[k] == "NA" or df[k] == "nil" or df[k] == "" or df[k] == "nan"):
            list.append(k)
            break
print(list)

# %% [markdown]
# ##### Replacing all the nil or nan values with 0

# %%
for df in data:
    for l in list:
        if(df[l] == "NA" or df[l] == "nil" or df[l] == "" or df[l] == "nan"):
            df[l] = "0"
        

# %% [markdown]
# #### Testing if the data is nil free

# %%
list = []
for k in data[0].keys():
    for df in data:
        if(df[k] == "NA" or df[k] == "nil" or df[k] == "" or df[k] == "nan"):
            list.append(k)
            break
print(list)


