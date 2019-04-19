from main import *
import numpy as np
import matplotlib.pyplot as plt

GRID = np.meshgrid(np.arange(0,10),np.arange(0,10))


## GRID[0] = x-coords GRID[1] = y-coords

# def initializeParticles(grid):
	# takes in the initial positions (aka, a grid)
	# and spits out an array of Dot objects

def isCollide(d1,d2):
	disp_vec = np.array(d1.pos)-np.array(d2.pos)
	# in other words 'about' the width of each dot
	return np.sqrt(np.dot(disp_vec,disp_vec)) <= 0.01
"""
new_vel_1 = old_vel_1 - (2*d2.mass/(d1.mass+d2.mass))*(np.dot(old_vel_1-old_vel_2,pos_1-pos_2)/(np.dot(pos_1-pos_2,pos_1-pos_2)))*(pos_1-pos_2)
new_vel_2 = old_vel_2 - (2*d1.mass/(d1.mass+d2.mass))*(np.dot(old_vel_2-old_vel_1,pos_2-pos_1)/(np.dot(pos_2-pos_1,pos_2-pos_1)))*(pos_2-pos_1)
"""

# a function that solves for new velocities using conservation of linear momentum
def momentumSolver(d1,d2):
	old_vel_1 = np.array(d1.vel)
	pos_1 = np.array(d1.pos)
	old_vel_2 = np.array(d2.vel)
	pos_2 = np.array(d2.pos)
	# nicked the formula below from wikipedia -- no idea how this _actually_ works.
	new_vel_1 = old_vel_1 - (np.dot(old_vel_1-old_vel_2,pos_1-pos_2)/(np.dot(pos_1-pos_2,pos_1-pos_2)))*(pos_1-pos_2)
	new_vel_2 = old_vel_2 - (np.dot(old_vel_2-old_vel_1,pos_2-pos_1)/(np.dot(pos_2-pos_1,pos_2-pos_1)))*(pos_2-pos_1)
	d1.vel = new_vel_1
	d2.vel = new_vel_2


dot_left = Dot(np.array([0.0,0.0]),np.array([0.5,0.5]),1.0)
dot_right = Dot(np.array([1.,0.]),np.array([-0.5,0.5]),1.0)
file_counter = 1
for t in np.linspace(0,10,100):
	# making the plots
	plt.ylim(0,1.5) # to make sure the 'camera' stays in one place
	plt.xlim(0,1.5)
	plt.scatter(dot_left.pos[0],dot_left.pos[1],c='r') # plotting the dots seprately as single dots.
	plt.scatter(dot_right.pos[0],dot_right.pos[1],c='k')
	plt.title("$t={}$ seconds".format(t)) # so i can keep track of the time as it ticks
	plt.savefig('random_move\\frame_{}.png'.format(file_counter)) # saving the file with the filecounter as the file numbering system
	file_counter+=1
	# post drawing, we check for collisions, because this is where the physics kicks
	# in, and we need to change things, kind of like how we take a picture and then
	# move objects in stop-motion animation.
	if isCollide(dot_left,dot_right):
		print("Collision detected!")
		momentumSolver(dot_left,dot_right)
	# position evolution hapens irrespective of collision, which is necessary
	# the dots won't move from their position where they've collided.
	dot_left.pos += dot_left.vel*(10/100)
	dot_right.pos += dot_right.vel*(10/100)
	# clearing the frame because otherwise we'll get smears instead of clear dots.
	plt.clf()
print("And we are done.")
