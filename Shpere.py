import numpy as np
# import pygame as pg
import random as rd
import math
from collections import namedtuple as nt

# class Spherical: # circle on a sphere described in spherical coordinates

#   def __init__(self, phi, theta, r, c_r):
#     self.phi = phi
#     self.theta = theta
#     self.r = r
#     self.c_r = c_r

class Vector:
  def __init__(self, angle, arc):
    self.angle = angle
    self.arc = arc

  def __str__(self):
    D = 5
    return ("Angle: " + str(round(self.angle, D)) +
            "  Arc: " + str(round(self.arc, D)))

class Sphirclical: # circle on a sphere described by its angle and arclength from (0, 0, 0)

  def __init__(self, theta, a):

    self.pos = Vector(theta, a)

  def update_pos(self, inst_vel):

    if inst_vel.angle == 0:
      self.pos.arc += inst_vel.arc
    elif inst_vel.angle == 180:
      self.pos.arc -= inst_vel.arc
    else:
      a = math.radians(self.pos.arc)
      b = math.radians(inst_vel.arc)
      C = math.radians(inst_vel.angle)

      c = math.acos(math.cos(a) * math.cos(b) +
                    math.sin(b) * math.sin(b) * math.cos(C))

      B = math.asin(math.sin(b) * math.sin(C) / math.sin(c))

      self.pos.angle = math.degrees(self.pos.angle + B) % 360
      self.pos.arc = math.degrees(c)

    self.clean_pos()

  def clean_pos(self):
    if self.pos.arc > 180:
      self.pos.arc = 360 - self.pos.arc
      self.pos.angle = (self.pos.angle + 180) % 360
    if self.pos.angle < 0:
      self.pos.angle += 360


class Game:

  def __init__(self):
    pass

  def Main():
    pass

def move_player(sph, angle, arc):

  sph.update_pos(Vector(sph.pos.angle - math.radians(angle),
                        math.radians(arc)))

def main():

  theta = -45  # position angle
  a = 0       # position magnitude
  p1 = Sphirclical(theta, a)
  
  C = 0
  b = 200
  iv = Vector(C, b)

  print(p1.pos)
  p1.update_pos(iv)
  print(p1.pos)

  # p1 = Sphirclical(theta, a)

  # print("Start:", p1.pos)
  # steps = 2
  # for i in range(steps):
  #   p1.update_pos()
  # print("End:  ", p1.pos)

if __name__ == '__main__':
  main()