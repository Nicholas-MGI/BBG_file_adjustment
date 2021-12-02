
# coding: utf-8

# In[18]:


import pandas as pd
from pathlib import Path
import csv


# In[19]:


file_path = Path(r"\\cator61ns1vf2\mgi\Projects\Charles River\RKS Files (Inbound Files)\2021\09 Sep\09.28.2021\SLH103_CA_20210929.csv")


upload_file = pd.read_csv(file_path, skiprows=1, error_bad_lines=False, sep ="|", header = None)


# In[10]:


manager_path = Path(r"\\cator61ns1vf2\mgi\Projects\Charles River\active_managers.csv")
active_managers = pd.read_csv(manager_path, skiprows=1, error_bad_lines=False,header = None)
active_managers = active_managers.values.tolist()
active_managers = list(map(''.join, active_managers))


# In[11]:


#line1 = upload_file.iloc[0,:]
#upload_file = upload_file.iloc[1:,:]
#upload_file.shape
#upload_file


# In[12]:


inclusion_list = [manager in active_managers for manager in upload_file.iloc[:,1].values]


# In[13]:


mid_upload = upload_file.loc[inclusion_list,:] #might need to append with line1 for upload


# In[14]:


#save_path = Path(r"\\cator61ns1vf2\mgi\Projects\Charles River\SLH103_CA_nick.csv")
save_path = Path(r"\\cator61ns1vf2\mgi\Projects\Charles River\RKS Files (Inbound Files)\2021\09 Sep\09.28.2021\SLH103_CA_20210929_nick_test.csv.csv")
mid_upload.to_csv(save_path, sep = "|",header = False, index = False)

