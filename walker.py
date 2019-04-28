#!python3


from particles import *
import matplotlib.pyplot as plt

part_system = [Dot(np.array([0,0]),np.array([0,1]),1.0) for i in range(100)]

def evolve(dot):
	velx = np.random.choice([-1,1])	
	dot.vel[0] = velx
	dot.pos += dot.vel
	dot.hist = np.vstack((dot.hist,dot.pos))


for t in range(100):
	for d in part_system:
		evolve(d)

# displaying all the paths undertaken by each dot
fig, ax = plt.subplots(1,1)
ax.set_xlim(-100,+100)
ax.set_ylim(-1,102)
ax.axvline(x=0.0)
for dot in part_system:
	ax.plot(dot.hist[:,0],dot.hist[:,1])
fig.savefig('scatter.png')