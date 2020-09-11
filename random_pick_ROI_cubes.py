# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:48:56 2020

@author: ajr71967
"""
import os
import random
from os import listdir
from os.path import isfile, join
import numpy as np
import shutil
method= 'to_pick' # 'to_drop'
nth=4 #####to pick, total file/1000, then lower round. to drop, total file/remove file then round
folder_to_analyse ='z_fixed_sampling/sample_123761/z_150/crop_img_25'######


mypath=folder_to_analyse
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
total_file=len(files)

random_num = random.randint(0,total_file-1)

filenum1=np.arange(random_num,total_file)
filenum2=np.arange(0,random_num)
filenum=np.concatenate((filenum1, filenum2), axis=0)

if len(np.unique(filenum))!=total_file:
    print ('file error')
    raise SystemExit
   
#to pick every nth file
if method == 'to_pick':
  selected_file=filenum[::nth]   
  if len(selected_file)>1000:
    
      selected_file_num = np.random.choice(selected_file, size=1000, replace=False)
  else:
      selected_file_num = selected_file    

  
#raise SystemExit
#to drop every nth file  
if method == 'to_drop':      
  selected_file = np.delete(filenum, np.arange(0, filenum.size, nth))

  if len(selected_file)>1000:
    
      selected_file_num = np.random.choice(selected_file, size=1000, replace=False)
  else:
      selected_file_num = selected_file    



if len(selected_file_num)!=1000:
    print ('selected_file_error')
    raise SystemExit



copy_from= folder_to_analyse
copy_to= folder_to_analyse+'/random_selected_cubes'

try:
    os.mkdir(copy_to)
except OSError:
    print ("Creation of the directory %s failed" %copy_to)
else:
    print ("Successfully created the directory %s " % copy_to)


for c in range (0,len(selected_file_num)):
 newPath = shutil.copy(copy_from+'/'+files[selected_file_num[c]], copy_to)



