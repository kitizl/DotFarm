#!python3


from particles import *
import numpy as np 
import matplotlib.pyplot as plt

part_system = [Dot(np.array([0,0]),np.array([0,1]),1.0) for i in range(100000000000)]

def evolve(dot):
	velx = np.random.choice([-1,1])	
	dot.vel[0] = velx
	dot.pos += dot.vel


for t in range(100):
	for d in part_system:
		evolve(d)

# make a list of all the positions

pos_list = np.array([abs(d.pos) for d in part_system])
print(pos_list)
print(pos_list[:,0])
print(pos_list[:,0].mean())
