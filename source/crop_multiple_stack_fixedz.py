# -*- coding: utf-8 -*-

import timeit
from skimage import io
import numpy as np
import os
import os.path
import random
start = timeit.default_timer()

im = io.imread('specimen1_data/data3_halfbinned_750vol.tif')


grid_type = 'cover_all' #'not_cover_all' 
NumOfImg =3#plus one of number of cubes in 1D 
z_thickness = 150 

if grid_type == 'cover_all':
    SizeOfVol = 750
    start = 0
else:
    included_vol =input('key in size of vol covered by grid') #grids that cover all vol = 750, grids not cover all = max vol that can go
    random_num = random.randint(0,750-int(included_vol))
    start = random_num # 0 for grids that cover all vol, random value for grids not cover all
    SizeOfVol = start+int(included_vol)
    if SizeOfVol>750:
        print('vol error')
        raise SystemExit



xloop = np.linspace(start,SizeOfVol,NumOfImg,dtype=int) #np.array([0,5,10,15])
yloop = xloop
zloop=np.linspace(0,750,(750/z_thickness)+1,dtype=int)

w = xloop[1]-xloop[0] # width
h = w # height
d = z_thickness # depth
save_path = "z_fixed_sampling/sample_123761/z_150/crop_img_"+str(w) 


try:
    os.mkdir(save_path)
except OSError:
    print ("Creation of the directory %s failed" %save_path)
else:
    print ("Successfully created the directory %s " % save_path)


tup = ()
c = 0

for xx in range(0,len(xloop)-1):   
    for yy in range(0,len(yloop)-1):
        for zz in range(0,len(zloop)-1):
            x = xloop[xx]
            y = yloop[yy]
            z = zloop[zz]
            for i in range(z,z+d):
                imcrop = im[i][y:y+h, x:x+w]
                np_image = np.array(imcrop)
                
                tup = tup + (np_image,) #add the image to the sequence
                final_image = np.stack(tup)
                
            fname = str(x) + '_' + str(x+w-1) +  '_' +\
            str(y) + '_' + str(y+h-1) +  '_' + \
            str(z) + '_' + str(i) + '.tif'
            print(fname)
            path = os.path.join(save_path, fname)  
            io.imsave(path, final_image)
            tup = ()
            
stop = timeit.default_timer()

print('Time: ', stop - start)              
