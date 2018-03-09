# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 01:20:45 2018

@author: Jie Lu
"""


import io

def test():
    file = io.open('task2/input.txt')
    char = file.read().strip('\n').strip()
    assert len(char) == 6