#!/usr/bin/env python
# coding: utf-8

# <h1 align="center">☁️ - Basic package 👨‍💻🔬</h1>
# 
# <h2 align="center">How to package code and re-use it</h2>
# <p style="text-align:center">
#    Thomas Bury<br>
#    Data Office<br>
#    Allianz<br>
# </p>
# 
# A basic package for illustrating how to package and distribute code. But also providing some classes and inheritance.
# 

# In[1]:


import numpy as np 
import pandas as pd
import yaml
from pprint import pprint

# Custom package
from pkgtemp.sub_pkg1.modA import Convoy, Motorcycle, Vehicle
from pkgtemp.sub_pkg1.modB import hello_world
from pkgtemp.sub_pkg2.modC import Complex
from pkgtemp.sub_pkg2.modD import Fibonacci 


# In[3]:


import pkgtemp
print(f'pkgtemp version {pkgtemp.__version__}')


# # Re-using your code
# ## Module modA - example of classes and inheritance

# In[2]:


moto1 = Motorcycle(passengers=['Pierre','Dimitri'], brand='Yamaha')
moto1.add('Yohann')
moto1.print_passengers()


# In[3]:


convoy1 = Convoy()
convoy1.vehicle_list[0].add('Albert')
convoy1.add_vehicle(Motorcycle(passengers=['Raphael'], brand='Honda'))


# In[4]:


for v in convoy1.vehicle_list:
    v.print_passengers() 


# ## Special methods - Comparison

# In[5]:


Complex(6, -3).__str__()


# In[6]:


# is the module of C1 smaller or larger than the module of C2
c1 = Complex(3, 4)
c2 = Complex(2, -5)
c1.__lt__(c2)


# ## Special methods - make a class instance callable

# In[7]:


# instanciate the class, which is a callable object thanks to the __call__ method
fibonacci_of = Fibonacci()


# In[8]:


fibonacci_of(5)


# In[9]:


fibonacci_of(12)


# # Load the config file for the paths
# To avoid to hardcode the paths in a versioned file, let's create a `paths.yml` which will **not** be versioned. So that the paths are not overwritten when we pull or merge from the GitHub repo. The `paths.yml` should have a structure like:
# 
# ```yml
# # data
# data:
#   test: "C:/Users/xtbury/Documents/Projects/segmentation_cloudy_regions/data/test_images"
#   train: "C:/Users/xtbury/Documents/Projects/segmentation_cloudy_regions/data/train_images"
#   docs: "C:/Users/xtbury/Documents/Projects/segmentation_cloudy_regions/data/"
# 
# # Path to store all notebooks, ideally not versioned
# notebooks: "C:/Users/xtbury/Documents/Projects/segmentation_cloudy_regions/notebooks/"
# 
# # Path to store all outputs (correlations, jsons, excel, etc)
# output: "C:/Users/xtbury/Documents/Projects/segmentation_cloudy_regions/output/"
# 
# # Path to store all python scripts, for versioning
# scripts: "C:/Users/xtbury/Documents/Projects/segmentation_cloudy_regions/scripts/"
# 
# # Path to studies
# studies: "C:/Users/xtbury/Documents/Projects/segmentation_cloudy_regions/studies/"
# ```
# 
# In the following cell, a user input field is created. Enter the path, without quotes.

# In[10]:


# Where is my yaml ? "C:/Users/xtbury/Documents/Projects/Pyreidolia/paths.yml"

paths_yml = input("where is the paths.yml config file?")
with open(paths_yml, "r") as ymlfile:
    path_dic = yaml.load(ymlfile, Loader=yaml.FullLoader)

pprint(path_dic)


# In[11]:


train_csv_path = path_dic['data']['docs'] + 'train.csv'
train_data = path_dic['data']['train'] 
test_data = path_dic['data']['test'] 


# In[12]:


train_csv_path

