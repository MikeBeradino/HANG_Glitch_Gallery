from art import *
#import numpy as np
import pyclbr
import random
import importlib
module_name = 'art'

y=[]

#loads array with art objects
for item in art.values():
    artname = str(item.name)
    y.append(artname)

#gets number of objects in the array
objects_inarray = len(y)

#gets random array element
random_object = random.randrange(0,objects_inarray)

#print y[random_object]
obj = eval(y[random_object] + "()")
