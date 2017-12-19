# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 22:12:13 2017

@author: Prathyusha Mallela
"""
#assignement 2.3
def reverse_string(string_to_be_reversed):
    reversed_string=string_to_be_reversed[::-1]; #this slice variation reverses the string
    return reversed_string;

string_to_be_reversed="AcadGild"
r=reverse_string(string_to_be_reversed);
print("The reversed string: \'",r,"\' of original string: \'",string_to_be_reversed,"\'");
