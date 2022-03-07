# Change format/extension code

import os
import sys
folder = 'C:/Users/Aswaad/Desktop/GIS-ite_clp_rsmplCode/' # change to folder of files to change
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.wld', '.jgw') # current, new ext
    output = os.rename(infilename, newname)
