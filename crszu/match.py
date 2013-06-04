#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import Image, ImageOps

def match(im):
    """
    Match single char image with all models, return matched value of char image.
    """
    diffs = []
    for model in os.listdir("images/models"):
        diffs.append(match_file(im, model))
    diffs.sort()
    return diffs[0][1][0]

def match_file(im, model_name):
    """
    Match two captchas, calculate their differences, return diff and modelname.
    """
    diff = 0
    im = Image.open(im)
    model = Image.open("images/models/"+ model_name)
    img = im.resize((15,20))
    model = model.resize((15,20))
    width, height = model.size
    imgp = img.load()
    modelp = model.load()
    for x in range(width):
        for y in range(height):
            if imgp[x,y] != modelp[x,y]:
                diff += 1
    return diff, model_name