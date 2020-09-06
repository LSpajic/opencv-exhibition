#!/usr/bin/python3
import sys
import cv2
import time
import math
import numpy as np
def draw_between(img,a,b, n):
	dx = round((a[0]-b[0])/(n))
	dy = round((a[1]-b[1])/(n))

	for k in range(0,n+1):
		img = cv2.circle(img,(dx*k+b[0],dy*k+b[1]),25, (0,255,0), -1)
	
	return img
	
def find_dots_between(a,b,n):
	dx = round((a[0]-b[0])/(n))
	dy = round((a[1]-b[1])/(n))
	tocke = []
	for k in range(0,n+1):
		x ,y = dx*k+b[0],dy*k+b[1]
		tocke.append((x,y))
	return tocke
def draw_chess_board(img, a, b, c,d,n):
	img = cv2.circle(img,a,30, (255,0,0), -1)
	#img = cv2.circle(img,b,30, (255,0,0), -1)
	#img = cv2.circle(img,c,30, (255,0,0), -1)
	#img = cv2.circle(img,d,30, (255,0,0), -1)
	img = cv2.line(img,a,b,(0,0,255),10)
	img = cv2.line(img,b,c,(0,0,255),10)
	img = cv2.line(img,c,d,(0,0,255),10)
	img = cv2.line(img,d,a,(0,0,255),10)
	ab = find_dots_between(a,b,n)
	bc = find_dots_between(b,c,n)
	dc = find_dots_between(d,c,n)
	ad = find_dots_between(a,d,n)
	parovi = []
	for i in range (0,n+1):
		parovi.append((ab[i],dc[i]))
#		parovi.append((bc[i],ad[i]))
	tocke_izmedju=[]
	for x in parovi:
		tocke_izmedju.append(find_dots_between(x[0],x[1],8))
	for y in range(0,8,2):
		for x in range (0,8,2):
			pts = np.array([tocke_izmedju[1+y][1+x],tocke_izmedju[1+y][0+x],tocke_izmedju[0+y][0+x],tocke_izmedju[0+y][1+x]], np.int32)
			pts = pts.reshape((-1,1,2))
			cv2.fillPoly(img,[pts],255)
	for y in range(1,9,2):
		for x in range (1,9,2):
			pts = np.array([tocke_izmedju[1+y][1+x],tocke_izmedju[1+y][0+x],tocke_izmedju[0+y][0+x],tocke_izmedju[0+y][1+x]], np.int32)
			pts = pts.reshape((-1,1,2))
			cv2.fillPoly(img,[pts],255)


	print(tocke_izmedju)
	#for x in range(0,8,2)
	#	tocke_izmedju[0][x]
	return img

def string_to_int_tuple(string):
	x,y = string.split(",")
	x,y = int(x),int(y)
	return x,y


def main(image_path, points_data_path):
    #ucitaj sliku
	img = cv2.imread(image_path)

    #ucitaj tocke
	metadata = open(points_data_path, 'r')
	a = string_to_int_tuple(metadata.readline())
	b = string_to_int_tuple(metadata.readline())
	c = string_to_int_tuple(metadata.readline())
	d = string_to_int_tuple(metadata.readline())

    #pozovi draw_chess_board s slikom i tockama kao argumentima
	img = draw_chess_board(img,a,b,c,d,8)
    #pokazi sliku sa sahovskom plocom

	img = cv2.resize(img, (int(img.shape[0]/5), int(img.shape[1]/5)))
	cv2.imshow("Sahovska ploca", img)
	cv2.waitKey(0)

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])