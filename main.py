#!/usr/bin/env python

import os
import json
from niftiMask2Surface import niftiMask2Surface

with open('config.json') as config_json:
    config = json.load(config_json)

pwd = os.getcwd()
os.mkdir(pwd + "/surfaces")
#os.chdir(pwd + "/surfaces")


aparcaseg = 'aparc+aseg.nii.gz'

filetype = config["filetype"]

labels = [4, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 43, 48, 50, 51, 52, 53,
          54, 55, 56, 72, 192, 85]
for e in labels:
    surfname = str(e)+'.'+ filetype
    niftiMask2Surface(e, aparcaseg, 'surfaces/'+surfname, 10, filetype)
