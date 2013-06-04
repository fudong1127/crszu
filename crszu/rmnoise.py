#!/usr/bin/env python
#-*- coding:utf-8 -*-

import Image
from errors import InvalidSizeError,SizeTypeError

def rmnoise(im, size=5, min_nbs=2):
    data = im.load()
    width, height = im.size
    for x in range(width):
        for y in range(height):
            if data[x,y] > 128:
                continue
            else:
                nbs = count_neighbors(data, width, height, x, y, size)
                if nbs < min_nbs:
                    data[x,y] = 255

def count_neighbors(data, w, h, x, y, size=3):

    nb = 0

    if not isinstance(size,int):
        raise SizeTypeError
    if size < 0 or size == size / 2 * 2:
        raise InvalidSizeError

    for i in range(x - ((size - 1) / 2), x + ((size - 1)) / 2):
        for j in range(y - ((size-1) / 2), y + ((size - 1)) / 2):
            if i < 0 or j < 0 or (x == i and y == j) or i >= w or j >= h:
                continue
            else:
                if data[i,j] == 1:
                    nb += 1
    return nb

