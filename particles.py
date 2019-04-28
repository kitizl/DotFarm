#!python3

import os
import numpy as np
# this file defines all the relevant objects that will be used

def createFolder(foldername):
	try:
		os.mkdir(foldername)
	except FileExistsError:
		print("Folder already exists.")
	return "shrug emoji"

def makeVideo(anim_generate_function,folder_name,framerate,outputfile):
	createFolder(folder_name)
	anim_generate_function(folder_name)
	os.system('ffmpeg -framerate {} -i frame_\%d.png {}.mp4'.format(framerate,outputfile))


class Dot:
	def __init__(self,pos,vel,mass):
		self.pos = pos
		self.vel = vel
		self.zero = self.pos
		self.mass = mass
		self.timer = 0
		self.hist =	np.array([self.pos])
# makeVideo(badWave,'images',50,"output")

