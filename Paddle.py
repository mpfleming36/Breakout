import pygame
import random
from Box import*
from Colors import*

class Paddle(Box):
    
    def _init_(self, x, y, width, height, vx, vy, color,boxType,health):
        Box.__init__(self, x, y, width, height, vx, vy, color,boxType,health)
        