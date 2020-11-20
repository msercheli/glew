# -*- coding: utf-8 -*-

name = 'glew'

version = '2.2.0'

authors = ['Nigel Stewart']

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")

uuid = "repository.glew"
