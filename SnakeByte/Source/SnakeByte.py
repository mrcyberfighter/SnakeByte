# -*- coding: utf-8 -*-

############################################################################
# This programm is under copyright from the GPL GNU GENERAL PUBLIC LICENSE #
############################################################################

import pygame
from pygame.locals import *
from sys import exit

from os.path import expanduser
from os import listdir

from time import sleep

import cPickle


 
class Level() :
  def __init__(self,start_direction,filename) :
    self.start_direction=start_direction
    self.file_level=file(filename,'rb') ;
    self.file_level_lines=self.file_level.readlines()
    self.file_level.close()
 
    self.phantom_counter=0
 
  def get_resolution(self) :
 
    return ((len(self.file_level_lines[0])*10),len(self.file_level_lines)*10+10)
 

  def get_start_snake_head_position(self) :
    return self.start_direction
 
 
  def compute_level_data(self,return_data) :
    barriers=[]
    snake_data=[]
    apples=[]
    phantom=[]
    exit=[]
    y=5
    for v in self.file_level_lines :
      x=5
      for z in v :
	if z == "H" :
	  barriers.append((x,y))

	elif z == "A" :
	  apples.append((x,y))

	elif z == "S" :
	  # snake head moved at the list begin for representation, by level file parsing.
	  # snake head always set to list begin.
	  snake_data.insert(0,(x,y))

	elif z == "s" :
	  if self.start_direction == "E" or self.start_direction == "S" :
	    # snake tail moved at the list end for representation,   by level file parsing.
	    # snake tail elements comes firts by parsing.
	    snake_data.insert(-1,(x,y))                                   
	  elif self.start_direction == "N" or self.start_direction == "W" :
	    # snake tail set at the list end for representation,   by level file parsing.
	    # snake tail elements comes later than the head by parsing.
	    snake_data.append((x,y))                                     

	elif z == "s" :
	  snake_data.append((x,y))

	elif z == "E" :
	  exit.append((x,y))

	x += 10
      y += 10
 
    if return_data == 'snake' :
      return snake_data
    elif return_data == 'apples' :
      return apples
    elif return_data == 'barriers' :
      return barriers
    elif return_data == 'exit' :
      return exit  


  def compute_phantom_mv_orientation(self,start_position,end_position) :
    if start_position == "U" and end_position == "D" :
      return (False,"V")
    elif start_position == "D" and end_position == "U" :
      return (False,"V")
    elif start_position == "L" and end_position == "R" :
      return ("H",False)
    elif start_position == "R" and end_position == "L" :
      return ("H",False)
    else :
      return ("H","V")


  def compute_phantom_next_mv(self,start_position,end_position) :
    if start_position == "U" and end_position == "D" :
      return "S"
    elif start_position == "D" and end_position == "U" :
      return "N"
    elif start_position == "L" and end_position == "R" :
      return "E"
    elif start_position == "R" and end_position == "L" :
      return "W"
 
    elif start_position == "UL" and end_position == "UR" :
      return "E"
    elif start_position == "UR" and end_position == "UL" :
      return "W"

    elif start_position == "DL" and end_position == "DR" :
      return "E"
    elif start_position == "DR" and end_position == "DL" :
      return "W"
 
    elif start_position == "UR" and end_position == "DR" :
      return "S"
    elif start_position == "UL" and end_position == "DL" :
      return "S"
 
 
    elif start_position == "DR" and end_position == "UR" :
      return "N"
    elif start_position == "DL" and end_position == "UL" :
      return "N"
 
 
  def compute_phantom_mv(self,start_position,end_position) :
    mv_list=[]
 
    if start_position == "U" and end_position == "D" :
      mv_list.append("U")
      mv_list.append("D")
      return (mv_list,"S")
    elif start_position == "D" and end_position == "U" :
      mv_list.append("D")
      mv_list.append("U")
      return (mv_list,"N")
    if start_position == "L" and end_position == "R" :
      mv_list.append("L")
      mv_list.append("R")
      return (mv_list,"E")
    elif start_position == "R" and end_position == "L" :
      mv_list.append("R")
      mv_list.append("L")
      return (mv_list,"W")
 
    elif start_position == "UL" and end_position == "DL" :
      mv_list.append("UL")
      mv_list.append("UR")
      mv_list.append("DR")
      mv_list.append("DL")
      # move directions list and
      # length computing orientation indicatoron
      return (mv_list,"E")
 
    elif start_position == "UL" and end_position == "UR" :
      mv_list.append("UL")
      mv_list.append("DL")
      mv_list.append("DR")
      mv_list.append("UR")
      # move directions list and
      # length computing orientation indicatoron
      return (mv_list,"S")
  
    elif start_position == "UR" and end_position == "DR" :
      mv_list.append("UR")
      mv_list.append("UL")
      mv_list.append("DL")
      mv_list.append("DR")
      # move directions list and
      # length computing orientation indicatoron
      return (mv_list,"W")
   
    elif start_position == "UR" and end_position == "UL" :
      mv_list.append("UR")
      mv_list.append("DR")
      mv_list.append("DL")
      mv_list.append("UL")
      # move directions list and
      # length computing orientation indicatoron
      return (mv_list,"S") 
 
    elif start_position == "DL" and end_position == "DR" :
      mv_list.append("DL")
      mv_list.append("UL")
      mv_list.append("UR")
      mv_list.append("DR")
      # move directions list and
      # length computing orientation indicatoron
      return (mv_list,"N")
 
    elif start_position == "DL" and end_position == "UL" :
      mv_list.append("DL")
      mv_list.append("DR")
      mv_list.append("UR")
      mv_list.append("UL")
      # move directions list and
      # length computing orientation indicatoron
      return (mv_list,"E")
 
    elif start_position == "DR" and end_position == "DL" :
      mv_list.append("DR")
      mv_list.append("UR")
      mv_list.append("UL")
      mv_list.append("DL")
      # move directions list and
      # length computing orientation indicatoron
      return (mv_list,"N")
   
    elif start_position == "DR" and end_position == "UR" :
      mv_list.append("DR")
      mv_list.append("DL")
      mv_list.append("UL")
      mv_list.append("UR")
      # move directions list and
      # length computing orientation indicatoron
      return (mv_list,"W") 

  def compute_phantoms(self) :
    i=0
    phantoms_datalist=[]
    switch_start_counter=False
    x=5
    while i < len(self.file_level_lines) :
      ii=0
      y=5
      while ii < len(self.file_level_lines[i]) :
	if self.file_level_lines[i][ii] == "G"  :
	  speed=4
	  start_position=""
	  end_position=""
	  if self.file_level_lines[i][ii-2] == 'U' :
	    start_position="U"
	  elif self.file_level_lines[i][ii-2] == 'D' :
	    start_position="D"
	  elif self.file_level_lines[i][ii-2] == 'L' :
	    start_position="L"
	  elif self.file_level_lines[i][ii-2] == 'R' :
	    start_position="R"

	  if self.file_level_lines[i][ii-1] == 'U' :
	    start_position += "U"
	  elif self.file_level_lines[i][ii-1] == 'D' :
	    start_position += "D"
	  elif self.file_level_lines[i][ii-1] == 'L' :
	    start_position += "L"
	  elif self.file_level_lines[i][ii-1] == 'R' :
	    start_position += "R"
       
          if self.file_level_lines[i][ii+1] == 'U' :
	    end_position="U"
	  elif self.file_level_lines[i][ii+1] == 'D' :
	    end_position="D"
	  elif self.file_level_lines[i][ii+1] == 'L' :
	    end_position="L"
	  elif self.file_level_lines[i][ii+1] == 'R' :
	    end_position="R"

	  if self.file_level_lines[i][ii+2] == 'U' :
	    end_position += "U"
	  elif self.file_level_lines[i][ii+2] == 'D' :
	    end_position += "D"
	  elif self.file_level_lines[i][ii+2] == 'L' :
	    end_position += "L"
	  elif self.file_level_lines[i][ii+2] == 'R' :
	    end_position += "R"
	 

          bool_compute_horizontal_length,bool_compute_vertical_length = self.compute_phantom_mv_orientation(start_position,end_position)
	  phantom_mv_datas=self.compute_phantom_mv(start_position,end_position)
      
          mv_list=phantom_mv_datas[0]
          direction=phantom_mv_datas[1]
       
          mv_len_x=0
          mv_len_y=0
          if bool_compute_horizontal_length :
	    if self.file_level_lines[i][ii+3] != "H" and self.file_level_lines[i][ii+3] != "E" :
	      i_c=0
	      while self.file_level_lines[i][ii+i_c] != "H" and self.file_level_lines[i][ii+i_c] != "E":
		i_c += 1
	      bool_compute_horizontal_length=False 
	  
	    elif self.file_level_lines[i][ii-3] != "H"and self.file_level_lines[i][ii-3] != "E" :
	      i_c=0
	      while self.file_level_lines[i][ii-i_c] != "H" and self.file_level_lines[i][ii-i_c] != "E":
		i_c += 1
	      bool_compute_horizontal_length=False   

	 
	    i_c -= 3
            mv_len_x=i_c

	  if bool_compute_vertical_length :
	    if self.file_level_lines[i+3][ii] != "H" and self.file_level_lines[i+3][ii] != "E":
	      i_c=0
	      while self.file_level_lines[i+i_c][ii] != "H" and self.file_level_lines[i+i_c][ii] != "E" :
		i_c += 1
	      bool_compute_vertical_length=False 

	    if self.file_level_lines[i-3][ii] != "H" and self.file_level_lines[i-3][ii] != "E" :
	      i_c=0
	      while self.file_level_lines[i-i_c][ii] != "H" and self.file_level_lines[i-i_c][ii] != "E" :
		i_c += 1
	      bool_compute_vertical_length=False 
	 
	    i_c -= 3
            mv_len_y=i_c
       
       
          start_coords=(y-10,x-10)
          phantoms_datalist.append(Phantom(direction,mv_list,mv_len_x,mv_len_y,start_coords,color=(255,0,0,255),speed=2))
       
        y += 10  
	ii += 1
      x += 10
      i += 1
 
    return phantoms_datalist

  def compute_barriers_collide_rect_list(self) :
    barriers_rect_list=level.compute_level_data('barriers')
    self.barriers_rect_list=[]
    for v in barriers_rect_list :
      self.barriers_rect_list.append(pygame.Rect(v,(10,10)))
  
  def compute_eat_apple_collide_rect_list(self) :
    apples_rect_list=level.compute_level_data('apples')
    self.apples_rect_list=[]
    for v in apples_rect_list :
      self.apples_rect_list.append(pygame.Rect(v,(10,10)))

  def compute_phantom_collide_rect_list(self) :
    self.phantom_rect_list=[]
    for phantoms in phantoms_entities :
      self.phantom_rect_list.append(pygame.Rect(phantoms.cur_coords,(30,30)))

 
  def compute_exit_collide_rect_list(self) :
    exit_barrier_list=level.compute_level_data('exit')
    self.exit_rect_list=[]
    for v in exit_barrier_list :
      self.exit_rect_list.append(pygame.Rect(v,(10,10)))






class Phantom() :
  def __init__(self,start_position,mv_list,mv_len_x,mv_len_y,start_coords,color,speed=2) :
    self.mv_list=mv_list   # List of the trajectories from the phantom in form of [START,END]               example: ["L","R"]             -> from Left to Right and reverse .          
                           #                                                   or [START,STEP_2,STEP_3,END] example: ["UL","UR","DR","DL"] -> UpLeft to UpRight to DownRight to DownLeft. ending chained to begin.
    self.cur_mv_list_idx=1 # Start index from the list of the trajectories to get direction to let the phantom go to.
 
    self.mv_len_x=mv_len_x # Units to go on in case of horizontal move (X axe) ;
    self.mv_len_y=mv_len_y # Units to go on in case of vertical move   (Y axe) ;
 
    # Computing if the phantom simply go on an axe or square move
    if mv_len_x and mv_len_y :
      # Phantom square moving.
      self.mv_x_and_y=True
    else :
      # Phantom linear moving.
      self.mv_x_and_y=False
   
    if start_position in ["N","S"] :
      self.bool_x=False
      self.bool_y=True
    else :
      self.bool_x=True
      self.bool_y=False
 
    self.cur_coords=start_coords # Current coordinate from the upper-left corner from the Phantom rectangle
 
    self.mv_counter_x=0
    self.mv_counter_y=0
 
 
  def compute_next_position(self) :
 
    if self.bool_x :
      # The current moving take place on the X axe.
      # So we check where to move the phantom.
      if ( (self.mv_list[self.cur_mv_list_idx] == "R") or  (self.mv_list[self.cur_mv_list_idx] == "UR" and self.mv_list[self.cur_mv_list_idx-1] == "UL") or (self.mv_list[self.cur_mv_list_idx] == "DR" and self.mv_list[self.cur_mv_list_idx-1] == "DL") ) and self.mv_counter_x < self.mv_len_x :
	# The phantom move from left to right on the X axe
	self.mv_counter_x += 1
	self.cur_coords=self.cur_coords[0]+10,self.cur_coords[1]

   
      elif ( (self.mv_list[self.cur_mv_list_idx] == "L") or (self.mv_list[self.cur_mv_list_idx] == "UL" and self.mv_list[self.cur_mv_list_idx-1] == "UR") or (self.mv_list[self.cur_mv_list_idx] == "DL" and self.mv_list[self.cur_mv_list_idx-1] == "DR") ) and self.mv_counter_x < self.mv_len_x :
	# The phantom move from left to right on the X axe
	self.mv_counter_x += 1
	self.cur_coords=self.cur_coords[0]-10,self.cur_coords[1]

 
   

   
      else :
	self.cur_mv_list_idx += 1 # Updating List of the trajectories index to get the new directionto go.
	self.mv_counter_x=0
	self.mv_counter_y=0
	if self.mv_x_and_y :
	  # Phantom square moving.
	  self.bool_x=False
	  self.bool_y=True
	else :
	  # Phantom linear moving.
	  self.bool_x=True
	  self.bool_y=False

        if self.cur_mv_list_idx == len(self.mv_list) :
	  # Reset List of the trajectories index to begin.
	  self.cur_mv_list_idx=0

  
    if self.bool_y :
      # The current moving take place on the Y axe.
      # So we check where to move the phantom.
      if ( (self.mv_list[self.cur_mv_list_idx] == "D") or (self.mv_list[self.cur_mv_list_idx] == "DR" and self.mv_list[self.cur_mv_list_idx-1] == "UR") or (self.mv_list[self.cur_mv_list_idx] == "DL" and self.mv_list[self.cur_mv_list_idx-1] == "UL") ) and self.mv_counter_y < self.mv_len_y :
	# The phantom move down on the Y axe
	self.mv_counter_y += 1
	self.cur_coords=self.cur_coords[0],self.cur_coords[1]+10

      elif ( (self.mv_list[self.cur_mv_list_idx] == "U") or (self.mv_list[self.cur_mv_list_idx] == "UR" and self.mv_list[self.cur_mv_list_idx-1] == "DR") or (self.mv_list[self.cur_mv_list_idx] == "UL" and self.mv_list[self.cur_mv_list_idx-1] == "DL") ) and self.mv_counter_y < self.mv_len_y :
	# The phantom move up on the Y axe
	self.mv_counter_y += 1
	self.cur_coords=self.cur_coords[0],self.cur_coords[1]-10
     
      else :
	self.cur_mv_list_idx += 1 # Updating List of the trajectories index to get the new directionto go.
	self.mv_counter_x=0
	self.mv_counter_y=0
	if self.mv_x_and_y :
	  # Phantom square moving.
	  self.bool_x=True
	  self.bool_y=False
	else :
	  # Phantom linear moving.
	  self.bool_x=False
	  self.bool_y=True

	if self.cur_mv_list_idx == len(self.mv_list) :
	  # Reset List of the trajectories index to begin.
	  self.cur_mv_list_idx=0







class Snake() :
  def __init__(self,start_direction,snake_coords,speed=0.15) :
    self.direction = self.head_position = start_direction
 
    self.snake_coords=snake_coords
    self.length=3
    self.anim_turn_length=1
    self.snake_speed=speed
 
  def forward(self) :
    if self.direction == "N" :
      tmp=[]
      for v in self.snake_coords :
	tmp.append((v[0],v[1]-10))
      self.snake_coords=tmp

    elif self.direction == "E" :
      tmp=[]
      for v in self.snake_coords :
	tmp.append((v[0]+10,v[1]))
      self.snake_coords=tmp
   
    elif self.direction == "W" :
      tmp=[]
      for v in self.snake_coords :
	tmp.append((v[0]-10,v[1]))
      self.snake_coords=tmp
   
    elif self.direction == "S" :
      tmp=[]
      for v in self.snake_coords :
	tmp.append((v[0],v[1]+10))
      self.snake_coords=tmp 


   
  def turn_right(self,length) :
 
    if self.direction == "N" :
      self.anim_turn_right_from_N(length)
   
    elif self.direction == "E" :
      self.anim_turn_right_from_E(length)
   
    elif self.direction == "S" :
      self.anim_turn_right_from_S(length)
  
    elif self.direction == "W" :
      self.anim_turn_right_from_W(length)
   
   
   
  def turn_left(self,length) :
 
    if self.direction == "N" :
      self.anim_turn_left_from_N(length)
 
    elif self.direction == "W" :
      self. anim_turn_left_from_W(length)
 
    elif self.direction == "S" :
      self.anim_turn_left_from_S(length)
 
    elif self.direction == "E" :
      self.anim_turn_left_from_E(length)

  def anim_turn_right_from_N(self,length) :
    if length < self.length :
      self.direction="N"
      tmp=[]
      i=0
      while i < length :
        tmp.append((self.snake_coords[i][0]+10,self.snake_coords[i][1]))
        i += 1
    
    
      i=length
      while i < self.length :
	tmp.append((self.snake_coords[i][0],self.snake_coords[i][1]-10))
	i += 1

      self.snake_coords=tmp
      self.anim_turn_length += 1 ;

      return

    else :
     # Turn right from N to E animation terminated
     self.anim_turn_length += 1 # Overflow the condition
     self.direction="E"         # Setting new direction value
  
    self.forward()
 

  def anim_turn_right_from_E(self,length) :
 
    if length < self.length :
      self.direction="E"
      tmp=[]
      i=0
      while i < length :
        tmp.append((self.snake_coords[i][0],self.snake_coords[i][1]+10))
        i += 1
 
      i=length
      while i < self.length :
        tmp.append((self.snake_coords[i][0]+10,self.snake_coords[i][1]))
        i += 1
     
      self.snake_coords=tmp
      self.anim_turn_length += 1 ;

      return
 
    else :
     # Turn right from E to S animation terminated
     self.anim_turn_length += 1 # Overflow the condition
     self.direction="S"         # Setting new direction value
  
    self.forward()
  
  def anim_turn_right_from_S(self,length) :
 
    if length < self.length :
      self.direction="S"
      tmp=[]
      i=0
      while i < length :
        tmp.append((self.snake_coords[i][0]-10,self.snake_coords[i][1]))
        i += 1
   
      i=length
      while i < self.length :
	tmp.append((self.snake_coords[i][0],self.snake_coords[i][1]+10))

	i += 1
      self.snake_coords=tmp
      self.anim_turn_length += 1 ;

      return
 
    else :
     # Turn right from S animation terminated
     self.anim_turn_length += 1 # Overflow the condition
     self.direction="W"         # Setting new direction value
  
    self.forward()

  def anim_turn_right_from_W(self,length) :
 
    if length < self.length :
      self.direction="W"
      tmp=[]
      i=0
      while i < length :
        tmp.append((self.snake_coords[i][0],self.snake_coords[i][1]-10))
        i += 1
   
      i=length
      while i < self.length :
	tmp.append((self.snake_coords[i][0]-10,self.snake_coords[i][1]))

	i += 1
      self.snake_coords=tmp
      self.anim_turn_length += 1 ;

      return
 
    else :
     # Turn right from W to N animation terminated
     self.anim_turn_length += 1 # Overflow the condition
     self.direction="N"  # Setting new direction value
  
    self.forward()

  def anim_turn_left_from_N(self,length) :
    if length < self.length :
      self.direction="N"
      tmp=[]
      i=0
      while i < length :
        tmp.append((self.snake_coords[i][0]-10,self.snake_coords[i][1]))
        i += 1
   
      i=length
      while i < self.length :
	tmp.append((self.snake_coords[i][0],self.snake_coords[i][1]-10))
	i += 1

      self.snake_coords=tmp
      self.anim_turn_length += 1 ;

      return
   
    else :
     # Turn left from N to W animation terminated
     self.anim_turn_length += 1  # Overflow the condition
     self.direction="W" # Setting new direction value
  
    self.forward()
  
  def anim_turn_left_from_W(self,length) :
 
    if length < self.length :
      self.direction="W"
      tmp=[]
      i=0
      while i < length :
        tmp.append((self.snake_coords[i][0],self.snake_coords[i][1]+10))
        i += 1
   
      i=length
      while i < self.length :
	tmp.append((self.snake_coords[i][0]-10,self.snake_coords[i][1]))

	i += 1
      self.snake_coords=tmp
      self.anim_turn_length += 1

      return
 
    else :
     # Turn left from W to S animation terminated
     self.anim_turn_length += 1 # Overflow the condition
     self.direction="S"  # Setting new direction value
  
    self.forward()

  def anim_turn_left_from_S(self,length) :
 
    if length < self.length :
      self.direction="S"
      tmp=[]
      i=0
      while i <length :
        tmp.append((self.snake_coords[i][0]+10,self.snake_coords[i][1]))
        i += 1
   
      i=length
      while i < self.length :
	tmp.append((self.snake_coords[i][0],self.snake_coords[i][1]+10))

	i += 1
      self.snake_coords=tmp
      self.anim_turn_length += 1 ;

      return
 
    else :
     # Turn left from S to E animation terminated
     self.anim_turn_length += 1 # Overflow the condition
     self.direction="E"         # Setting new direction value
  
    self.forward()

  def anim_turn_left_from_E(self,length) :
 
    if length < self.length :
      self.direction="E"
      tmp=[]
      i=0
      while i < length :
        tmp.append((self.snake_coords[i][0],self.snake_coords[i][1]-10))
        i += 1
 
      i=length
      while i < self.length :
        tmp.append((self.snake_coords[i][0]+10,self.snake_coords[i][1]))
        i += 1
     
      self.snake_coords=tmp
      self.anim_turn_length += 1 ;

      return
 
    else :
     # Turn left from E to N animation terminated
     self.anim_turn_length += 1 # Overflow the condition
     self.direction="N"         # Setting new direction value
  
    self.forward()
  
  def anim_slide_right(self) :
    tmp=[]
    if self.direction == "N" :
      for v in self.snake_coords :
        tmp.append((v[0]+10,v[1]))
  
    elif self.direction == "E" :
      for v in self.snake_coords :
        tmp.append((v[0],v[1]+10))
     
    elif self.direction == "S" :
      for v in self.snake_coords :
        tmp.append((v[0]-10,v[1]))
     
    elif self.direction == "W" :
      for v in self.snake_coords :
        tmp.append((v[0],v[1]-10))
     
    self.snake_coords=tmp
    self.forward()
 
  def anim_slide_left(self) :
    tmp=[]
    if self.direction == "N" :
      for v in self.snake_coords :
        tmp.append((v[0]-10,v[1]))
  
    elif self.direction == "E" :
      for v in self.snake_coords :
        tmp.append((v[0],v[1]-10))
     
    elif self.direction == "S" :
      for v in self.snake_coords :
        tmp.append((v[0]+10,v[1]))
     
    elif self.direction == "W" :
      for v in self.snake_coords :
        tmp.append((v[0],v[1]+10))
     
    self.snake_coords=tmp
    self.forward()
  
  def get_snake_position_rect_list(self) :
    snake_rect_list=[]
    for v in snake.snake_coords :
      snake_rect_list.append(pygame.Rect(v,(10,10)))
  
    return snake_rect_list
 

  


class Playground() :
  def __init__(self,apples_coords,barriers_coords,exits,snake_color,background_color) :
 
    self.apples_coords=apples_coords
    self.barriers_coords=barriers_coords
    self.exit_coords=exits
 
    self.snake_color=snake_color
    self.snake_color_back_up=snake_color
 
 
    self.apples_color_center=(255,255,0,255)
    self.apples_color_circle=(255,255,255,255)
 
    self.barriers_color_1=(211,211,211,255)
    self.barriers_color_2=(137,0,137,255)
 
    self.exit_color_1=[(211,211,211,255),(211,211,211,255),(211,211,211,255),(211,211,211,255),(211,211,211,255)]
    self.exit_color_2=[(137,0,137,255),(137,0,137,255),(137,0,137,255),(137,0,137,255),(137,0,137,255)]
 
    self.phantoms_color_1=(211,211,211,255)
    self.phantoms_color_2=(137,0,137,255)
 
 

 
    self.background_color=background_color
 
 
    self.blink_colors=[(211,211,211,255),(137,0,137,255)]
    self.losing_bink_time=16
 
    self.countdown=-2
 
    self.level=level
 
 
  def draw_playground(self) :

    for v in snake.snake_coords :
      pygame.draw.rect(screen,self.snake_color,((v[0],v[1]),(9,9)),0)
 
    for v in self.apples_coords :
      pygame.draw.circle(screen,self.apples_color_center,(v[0]+5,v[1]+5),6,0)
      pygame.draw.circle(screen,self.apples_color_circle,(v[0]+5,v[1]+5),6,1)
 
    for phantoms in phantoms_entities :

	pygame.draw.polygon(screen,self.phantoms_color_1,[(phantoms.cur_coords[0],phantoms.cur_coords[1]+9),(phantoms.cur_coords[0]+9,phantoms.cur_coords[1]),(phantoms.cur_coords[0]+18,phantoms.cur_coords[1]),(phantoms.cur_coords[0]+27,phantoms.cur_coords[1]+9),(phantoms.cur_coords[0]+27,phantoms.cur_coords[1]+18),(phantoms.cur_coords[0]+18,phantoms.cur_coords[1]+27),(phantoms.cur_coords[0]+9,phantoms.cur_coords[1]+27),(phantoms.cur_coords[0],phantoms.cur_coords[1]+18)] ,0)
	pygame.draw.polygon(screen,self.phantoms_color_2,[(phantoms.cur_coords[0],phantoms.cur_coords[1]+9),(phantoms.cur_coords[0]+9,phantoms.cur_coords[1]),(phantoms.cur_coords[0]+18,phantoms.cur_coords[1]),(phantoms.cur_coords[0]+27,phantoms.cur_coords[1]+9),(phantoms.cur_coords[0]+27,phantoms.cur_coords[1]+18),(phantoms.cur_coords[0]+18,phantoms.cur_coords[1]+27),(phantoms.cur_coords[0]+9,phantoms.cur_coords[1]+27),(phantoms.cur_coords[0],phantoms.cur_coords[1]+18)] ,1)

	pygame.draw.circle(screen, self.phantoms_color_2, (phantoms.cur_coords[0]+9,phantoms.cur_coords[1]+9), 4, 0)
	pygame.draw.circle(screen, self.phantoms_color_2, (phantoms.cur_coords[0]+9+9,phantoms.cur_coords[1]+9), 4, 0)
	pygame.draw.rect(screen,self.phantoms_color_1,((phantoms.cur_coords[0]+7,phantoms.cur_coords[1]+7),(4,4)),0)
	pygame.draw.rect(screen,self.phantoms_color_1,((phantoms.cur_coords[0]+7+9,phantoms.cur_coords[1]+7),(4,4)),0)

	pygame.draw.ellipse(screen, self.barriers_color_2, ((phantoms.cur_coords[0]+5,phantoms.cur_coords[1]+16),(27-9,9)), 2)
     
    for v in self.barriers_coords :
      # You can switch in an unicolor modus by overwriting the color displaying order !
      pygame.draw.rect(screen,self.barriers_color_1,(v,(9,9)),0)
      pygame.draw.rect(screen,self.barriers_color_2,((v[0]+3,v[1]+3) ,(3,3)),0)
 
 
  
    i=0
    while i <  len(self.exit_coords) :
      if game_control.exit_closed :
        pygame.draw.rect(screen,self.exit_color_1[i],(self.exit_coords[i],(9,9)),0)
        pygame.draw.rect(screen,self.exit_color_2[i],((self.exit_coords[i][0]+3,self.exit_coords[i][1]+3) ,(3,3)),0)
      i += 1
   
  def check_eat_apple_colliding(self) :
    snake_positions=snake.get_snake_position_rect_list()

    for v in snake_positions :
      apple_eat=v.collidelist(level.apples_rect_list)
      if apple_eat != -1 :
        break
     
    if apple_eat != -1 :
      # Snake eat an apple.
      game_sound.eat_apple_sound_play()
      self.apples_coords.pop(apple_eat)
      level.apples_rect_list.pop(apple_eat)
      game_control.apple_counter += 1
   
    if level.apples_rect_list == [] :
      return 1
    else :
      return False
   
  def check_barriers_colliding(self) :
    snake_positions=snake.get_snake_position_rect_list()
    is_snake_colliding=False
    for v in snake_positions :
      if v.collidelist(level.barriers_rect_list) != -1 :
	game_control.animation_blocking=True
	game_control.animation_losing=True
	game_sound.losing_sound_play()

	is_snake_colliding=True
	break
    if game_control.exit_closed :
      for v in snake_positions :
	if v.collidelist(level.exit_rect_list) != -1 :
	  game_control.animation_blocking=True
	  game_control.animation_losing=True
	  game_sound.losing_sound_play()

	  is_snake_colliding=True
	  break
	 
    return is_snake_colliding

  def check_snake_go_exit(self) :
    snake_positions=snake.get_snake_position_rect_list()
    is_snake_colliding=False
    if not game_control.exit_closed :
      for v in snake_positions :
	if v.collidelist(level.exit_rect_list) != -1 :


	  is_snake_colliding=True
	  break
	 
    return is_snake_colliding
 

  def check_phantom_colliding(self) :
    snake_positions=snake.get_snake_position_rect_list()
    is_snake_colliding=False
    for v in snake_positions :
      ret=v.collidelist(level.phantom_rect_list)
      if ret != -1 :
	# Snake collide an phantom.
	game_control.animation_blocking=True
	game_control.animation_losing=True
	game_sound.losing_sound_play()

	is_snake_colliding=True
	break
 
    return is_snake_colliding
 


  def barriers_color_inversing(self) :
    tmp=self.barriers_color_2
    self.barriers_color_2=self.barriers_color_1
    self.barriers_color_1=tmp

  def exit_color_inversing(self,i) :
    tmp=self.exit_color_1[i]
    self.exit_color_1[i]=self.exit_color_2[i]
    self.exit_color_2[i]=tmp
 
  def phantoms_color_inversing(self) :
    tmp=self.phantoms_color_2
    self.phantoms_color_2=self.phantoms_color_1
    self.phantoms_color_1=tmp

  def set_snake_color_start_animation(self,color) :
    if color % 2 == 0 :
      self.snake_color=playground.background_color
    else :
      self.snake_color=self.snake_color_back_up

 
  def losing_blink_snake(self) :
 
    self.snake_color=self.blink_colors[self.losing_bink_time % 2]
    self.barriers_color_inversing()
    self.phantoms_color_inversing()
    self.losing_bink_time -= 1
 


  def losing_change_snake_color_gradient(self) :
   if self.countdown == self.countdown_max :
     return False
   else :
     self.snake_color=self.losing_gradient[self.countdown]
     self.countdown += 1
     return True

  def losing_compute_down_gradient(self) :

    self.losing_gradient=[]
    if self.background_color == (255,0,255,255) :
      i=128+64+32+16 # correct to 127+63+31+16
      while i < 256 :

	self.losing_gradient.append((i,0,i,255))
	i += 4
  
    elif self.background_color == (0,255,255,255) :
      i=128+64+32+16 # correct to 127+63+31+16
      while i < 256 :

	self.losing_gradient.append((0,i,i,255))
	i += 4
    elif self.background_color == (0,0,255,255) :
      i=128+64+32+16 # correct to 127+63+31+16
      while i < 256 :

	self.losing_gradient.append((0,0,i,255))
	i += 4
    elif self.background_color == (0,255,0,255) :
      i=128+64+32+16 # correct to 127+63+31+16
      while i < 256 :

	self.losing_gradient.append((0,i,0,255))
	i += 4
    elif self.background_color == (255,0,0,255) :
      i=128+64+32+16 # correct to 127+63+31+16
      while i < 256 :

	self.losing_gradient.append((i,0,0,255))
	i += 4

    elif self.background_color == (127,127,127,255) :
      i=64+32+16
      while i < 128 :

	self.losing_gradient.append((i,i,i,255))
	i += 4
    elif self.background_color == (191,191,191,255) :
      i=176
      while i < 192 :

	self.losing_gradient.append((i,i,i,255))
	i += 4
    elif self.background_color == (0,0,0,255) :
      i=16 # correct to 127+63+31+16
      while i > 0 :

	self.losing_gradient.append((i,i,i,255))
	i -= 4
    self.countdown_max=len(self.losing_gradient)


  def phamtoms_forward(self) :
    for v in phantoms_entities :
      v.compute_next_position()
    self.phantoms_color_inversing()

  def start_animation_exit_open(self) :
    game_sound.exit_open_play()
    game_control.animation_exit_open_running=True
    playground.barriers_color_inversing()
    next_step_anim_event=pygame.event.Event(USEREVENT, {'code' : "opening_animation"} )
    pygame.event.post(next_step_anim_event)

  def set_animation_exit_open_next(self) :
    if game_control.animation_exit_open_colors_idx < 5 and not game_control.animation_exit_open_reverse and game_control.animation_exit_open_counter < 6 :
      self.exit_color_inversing(game_control.animation_exit_open_colors_idx)
      game_control.animation_exit_open_colors_idx += 1
   
    elif game_control.animation_exit_open_colors_idx == 5 and game_control.animation_exit_open_counter < 6 :
      game_control.animation_exit_open_reverse=True
      game_control.animation_exit_open_counter += 1
      game_control.animation_exit_open_colors_idx -= 1
    elif game_control.animation_exit_open_colors_idx >= 0 and game_control.animation_exit_open_reverse and game_control.animation_exit_open_counter < 6 :
      self.exit_color_inversing(game_control.animation_exit_open_colors_idx)
      game_control.animation_exit_open_colors_idx -= 1   
    elif game_control.animation_exit_open_colors_idx == -1 and game_control.animation_exit_open_counter < 6 :
      game_control.animation_exit_open_reverse=False
      game_control.animation_exit_open_counter += 1
      game_control.animation_exit_open_colors_idx += 1
    else :
      self.barriers_color_inversing()
      game_control.animation_exit_open_running=False
      game_control.exit_closed=False


class Game_control() :
  def __init__(self,apples_total) :
    # Snake move boolean control
    self.animation_blocking=False
    self.animation_turning_right=False
    self.animation_turning_left=False
    self.animation_losing=False
    self.animation_slide=False
 
    # Phantoms move condition
    self.animate_phantom=True
 
    # Open exit animation boolean control
    self.animate_exit_open=False
    self.exit_closed=True
    self.animation_exit_open_colors_idx=0
    self.animation_exit_open_reverse=False
    self.animation_exit_open_counter=0
    self.animation_exit_open_running=False
 
    self.animate_start_game=True

    self.all_apples_eat=False
 
    self.snake_lifes=10
 
    self.snake_stop=False
 
    self.apples_total=apples_total
 
    self.apple_counter=0
 
    self.snake_player_win=False
 
    self.game_over_text_display=False
    self.game_over_summary_text_display=False
    self.registering_score_answers="NO"
 
    self.game_over=False
 
  def set_animation_blocking_on(self) :
    self.animation_blocking=True
 
  def set_animation_blocking_off(self) :
    self.animation_blocking=False
    self.animation_turning_right=False
    self.animation_turning_left=False
    self.animation_slide=False
 
  def set_animation_turning_right_on(self) :
    self.animation_turning_right=True
    self.animation_turning_left=False
 
  def set_animation_turning_left_on(self) :
    self.animation_turning_left=True
    self.animation_turning_right=False

  def set_animation_sliding_on(self) :
    self.animation_slide=True
    self.animation_blocking=True
    self.animation_turning_right=False
    self.animation_turning_left=False

  def set_animation_sliding_off(self) :
    self.animation_slide=False
    self.animation_blocking=False
    self.animation_turning_right=False
    self.animation_turning_left=False


   
   

class Game_sound() :
  def __init__(self) :
    self.user_directory="/usr/share"
    self.game_path=self.user_directory+"/SnakeByte/"
    self.snake_turn_from_left_sound_filepath=self.game_path+"Sound/snake_mv/Arrow_Right_To_Left.wav"
    self.snake_turn_from_right_sound_filepath=self.game_path+"Sound/snake_mv/Arrow_Left_To_Right.wav"
    self.snake_turn_from_slide_sound_filepath=self.game_path+"/Sound/snake_mv/Arrow.wav"
    self.snake_eat_apple_sound_filepath=self.game_path+"Sound/snake_slurp/snake_eat_apple_sound.wav"
    self.losing_bink_sound_filepath=self.game_path+"Sound/game_over/Snakebyte_losing_rattle.wav"
    self.exit_open_sound_filepath=self.game_path+"Sound/open_exit/SnakeByte_Exit_open_rattle.wav"

    self.snake_turn_from_left_sound_object=pygame.mixer.Sound(self.snake_turn_from_left_sound_filepath)
    self.snake_turn_from_right_sound_object=pygame.mixer.Sound(self.snake_turn_from_left_sound_filepath)
    self.snake_turn_from_slide_sound_object=pygame.mixer.Sound(self.snake_turn_from_left_sound_filepath)
    self.snake_eat_apple_sound_object=pygame.mixer.Sound(self.snake_eat_apple_sound_filepath)
    self.losing_bink_sound_object=pygame.mixer.Sound(self.losing_bink_sound_filepath)
    self.exit_open_sound_object=pygame.mixer.Sound(self.exit_open_sound_filepath)
 
    self.snake_turn_from_left_sound_object.set_volume(0.2)
    self.snake_turn_from_right_sound_object.set_volume(0.2)
    self.snake_turn_from_slide_sound_object.set_volume(0.2)
    self.snake_eat_apple_sound_object.set_volume(0.25)
    self.losing_bink_sound_object.set_volume(0.25)
    self.exit_open_sound_object.set_volume(0.25)
 
    self.background_music_filepath=self.user_directory+"/SnakeByte/"+"/Sound/bg/SnakeByte_bg.wav"
 
 
 

 
  def init_threads(self) :
    self.thread_losing_blink_sound=Thread(group=None, target=game_sound.losing_sound_play, name="Losing blink animation thread", args=(), kwargs=None, verbose=None)

  def turn_left_sound_play(self) :
 
    self.snake_turn_from_left_sound_object.play()
 
  def turn_right_sound_play(self) :
 
    self.snake_turn_from_right_sound_object.play()
 
  def turn_slide_sound_play(self) :
   
    self.snake_turn_from_slide_sound_object.play()

  def eat_apple_sound_play(self) :
 
    self.snake_eat_apple_sound_object.play()

  def losing_sound_play(self) :
 
    self.losing_bink_sound_object.play()

  def exit_open_play(self) :
 
    self.exit_open_sound_object.play()

  def background_music_start(self) :
    self.background_music_object=pygame.mixer.music.load(self.background_music_filepath)
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)



class Animations_sounds() :
  def __init__(self) :
    self.user_directory="/usr/share"
    self.game_path=self.user_directory+"/SnakeByte/"
    self.intro_animation_music_filepath=self.game_path+"Sound/intro/intro_music.wav"
    self.start_sound_filepath=self.game_path+'Sound/animation/SnakeByte_intro_rattle.wav'
 
    self.snake_rattle_sound_filepath=self.game_path+"Sound/animation/SnakeByte_level_choice_rattle.wav"
 
  def play_rattle_start_animation(self) :
    self.start_sound_object=pygame.mixer.Sound(self.start_sound_filepath)
    self.start_sound_object.play()
 
  def play_rattle_select_level(self) :
    self.select_level_sound_object=pygame.mixer.Sound(self.snake_rattle_sound_filepath)
    self.select_level_sound_object.play()

  def set_intro_music_start(self) :
    self.intro_animation_music_object=pygame.mixer.music.load(self.intro_animation_music_filepath)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)

class Game_text() :
  def __init__(self) :
    self.big_font_size=128+32+64
    self.big_font=pygame.font.Font(None,self.big_font_size)
    self.little_font_size=64+16
    self.little_font=pygame.font.Font(None,self.little_font_size)
    self.highscores_font_size=64
    self.highscores_font=pygame.font.SysFont("Monospace",self.highscores_font_size,True)

class Highscores() :
  def __init__(self) :
    self.user_directory="/usr/share"
    self.highscore_fuchsia_labyrinth_filepath=self.user_directory+"/SnakeByte/Highscores/fuchsia_labyrinth_highscores.pkl"
    self.highscore_turkish_labyrinth_filepath=self.user_directory+"/SnakeByte/Highscores/turkish_labyrinth_highscores.pkl"
    self.highscore_blue_labyrinth_filepath=self.user_directory+"/SnakeByte/Highscores/blue_labyrinth_highscores.pkl"
    self.highscore_silver_labyrinth_filepath=self.user_directory+"/SnakeByte/Highscores/silver_labyrinth_highscores.pkl"
    self.highscore_darkgray_labyrinth_filepath=self.user_directory+"/SnakeByte/Highscores/darkgray_labyrinth_highscores.pkl"
    self.highscore_green_labyrinth_filepath=self.user_directory+"/SnakeByte/Highscores/green_labyrinth_highscores.pkl"
    self.highscore_red_labyrinth_filepath=self.user_directory+"/SnakeByte/Highscores/red_labyrinth_highscores.pkl"
    self.highscore_black_labyrinth_filepath=self.user_directory+"/SnakeByte/Highscores/black_labyrinth_highscores.pkl"
 
  def register_highscore(self,user_object,level) :
 
    self.highscore_filepath=self.select_file(level)
 
    self.pickle_file=open(self.highscore_filepath, 'rb')
    try :
      self.highscore_list=cPickle.load(self.pickle_file)
    except :
      self.highscore_list=[]
    self.pickle_file.close()
    self.highscore_list.append((user_object.username,user_object.percent,user_object.apple_eat,user_object.apple_total))
    self.pickle_file=open(self.highscore_filepath, 'wb')
    cPickle.dump(self.highscore_list,self.pickle_file,-1)
    self.pickle_file.close()

  def get_highscores(self,level) :
    self.highscore_filepath=self.select_file(level)
    self.pickle_file=open(self.highscore_filepath, 'rb')
    try :
      self.highscore_list=cPickle.load(self.pickle_file)
    except :
      self.highscore_list=[]
    self.pickle_file.close()
    return sorted(self.highscore_list,key=self.sorting_key)
 
  def sorting_key(self,data) :
    return data[1]
 
  def select_file(self,level) :
    if level == 0 :
      return self.highscore_fuchsia_labyrinth_filepath
    elif level == 1 :
      return self.highscore_turkish_labyrinth_filepath
    elif level == 2 :
      return self.highscore_blue_labyrinth_filepath
    elif level == 3 :
      return self.highscore_silver_labyrinth_filepath
    elif level == 4 :
      return self.highscore_darkgray_labyrinth_filepath
    elif level == 5 :
      return self.highscore_green_labyrinth_filepath
    elif level == 6 :
      return self.highscore_red_labyrinth_filepath
    elif level == 7 :
      return self.highscore_black_labyrinth_filepath
 

 
class Username() :
  def __init__(self,username,apple_eat,apple_total, percent) :
    self.username=username
    self.apple_eat=apple_eat
    self.apple_total=apple_total
    self.percent=percent


class Game_mainloop_control() :
  def __init__(self) :
 
    self.start_side_static=False
    self.from_level_selecting=False
    self.from_game=False
 
 
    self.animate_next_level=False
    self.animate_next_level_end=False
    self.animate_level_title_font=64
    self.animate_level_title_lt=False
    self.animate_level_title_gt=False
 
    self.is_animating=False
    self.is_animation_intro_running=True
    self.choose_level_sleep=0
    self.button_pressed=False
    self.level_image_is_display=True
 
class Game_mainloop() :

  def __init__(self) :
 
    pygame.init()
    pygame.display.set_caption("SnakeByte")
    self.user_dir="/usr/share"
 
    self.intro_animation_dir=self.user_dir+"/SnakeByte/Anim/animation_intro/"
    self.tiny_snakes_dir=self.user_dir+"/SnakeByte/Anim/tiny_snakes/"
    self.levels_files_dir=self.user_dir+"/SnakeByte/Levels/"
    self.levels_static_files_dir=self.user_dir+"/SnakeByte/Anim/Levels/"
    self.levels_files=['playground_level_01_fuchsia.txt',   # Snake green
			'playground_level_02_turkish.txt',   # Snake red
			'playground_level_03_blue.txt',      # Snake green
			'playground_level_04_silver.txt',    # Snake red
			'playground_level_05_darkgray.txt',  # Snake green
			'playground_level_06_green.txt',     # Snake red
			'playground_level_07_red.txt',       # Snake green
			'playground_level_08_black.txt'      # Snake red
			]
    self.iconfy_icon=pygame.image.load(self.user_dir+"/SnakeByte/Icon/SnakeByte_iconify.png")
 
    pygame.display.set_icon(self.iconfy_icon)
    self.levels_names=["Fuchsia Labyrinth","turkish Labyrinth","Blue Labyrinth","Silver Labyrinth","Darkgray Labyrinth","Green Labyrinth","Red Labyrinth","Black Labyrinth"]
 
    self.levels_background_colors=[(255,0,255,255),(0,255,255,255),(0,0,255,255),(191,191,191,255),(127,127,127,255),(0,255,0,255),(255,0,0,255),(0,0,0,255)]
    self.levels_snake_colors=[(0,255,0,255),(255,0,0,255),(0,255,0,255),(255,0,0,255),(0,255,0,255),(255,0,0,255),(0,255,0,255),(255,0,0,255)]
    self.levels_snale_start_orientation=["E","N","N","E","E","S","N","E"]
 
 
    self.tiny_snake_left_green_image=pygame.image.load(self.tiny_snakes_dir+"snake_skp_img_tiny_green_left_128.png")
    self.tiny_snake_left_green_image.set_colorkey((0,0,0,255),0)
    self.tiny_snake_right_green_image=pygame.image.load(self.tiny_snakes_dir+"snake_skp_img_tiny_green_right_128.png")
    self.tiny_snake_right_green_image.set_colorkey((0,0,0,255),0)
 
    self.tiny_snake_left_red_image=pygame.image.load(self.tiny_snakes_dir+"snake_skp_img_tiny_red_left_128.png")
    self.tiny_snake_left_red_image.set_colorkey((0,0,0,255),0)
    self.tiny_snake_right_red_image=pygame.image.load(self.tiny_snakes_dir+"snake_skp_img_tiny_red_right_128.png")
    self.tiny_snake_right_red_image.set_colorkey((0,0,0,255),0)
 
    self.tiny_snakes_left_images=[self.tiny_snake_left_green_image,self.tiny_snake_left_red_image]
    self.tiny_snakes_right_images=[self.tiny_snake_right_green_image,self.tiny_snake_right_red_image]
 
    self.levels_tiny_images=[pygame.image.load(self.levels_static_files_dir+'01_Fuchsia_Labyrinth.png'),
pygame.image.load(self.levels_static_files_dir+'02_Turksih_Labyrinth.png'),
pygame.image.load(self.levels_static_files_dir+'03_Blue_Labyrinth.png'),
pygame.image.load(self.levels_static_files_dir+'04_Lightgray_Labyrinth.png'),
pygame.image.load(self.levels_static_files_dir+'05_Darkgray_Labyrinth.png'),
pygame.image.load(self.levels_static_files_dir+'06_Green_Labyrinth.png'),
pygame.image.load(self.levels_static_files_dir+'07_Red_Labyrinth.png'),
pygame.image.load(self.levels_static_files_dir+'08_Black_Labyrinth.png')]
 
    self.show_game_title=False
    self.title_font_size=0
 
    self.level_anim_x=980
    self.level_anim_y=552
 
    self.show_game_title=False
    self.show_level_choice=False
 
    self.level_tiny_images_index=0
 
    self.level_tiny_next_images_index=1
    self.level_tiny_prev_images_index=7
 
    self.font_select_level_message=pygame.font.SysFont("San-Serif", 48, True, False)
 
    self.font_select_level_title=pygame.font.SysFont("San-Serif", 64, True, False)
 
    self.goto_select_level_strings="Hit Enter to select a level"
 
    self.select_level_string="Hit Enter to play this level"
    self.select_highscore_string="Hit Space to sea highscores"
    self.blink_choice_color=[(0,255,0),(255,0,0)]
 
 
    self.level_name_index=0
    self.level_name_selecting=self.levels_names[self.level_name_index]
 
 
 
  def show_level_presentation(self) :
 
    pygame.display.set_caption("SnakeByte")
    pygame.display.set_icon(self.iconfy_icon)
 
    screen=pygame.display.set_mode((980, 680),0,32)
 
    game_mainloop_control.from_level_selecting=True
    run=True
 
    font_buttons=pygame.font.SysFont("San-Serif", 24, True, False)
 
    self.prev_button_color=(0,255,0)
    self.next_button_color=(0,255,0)
    self.prev_button_text_color=(0,0,0)
 
    self.prev_button_text="    PREV  "
    self.prev_button_text_x=50-21
    self.prev_button_text_y=54/2.-7.5
    self.prev_button_arrow_right_x=50-21
    self.prev_button_arrow_right_y_down=54
    self.prev_button_arrow_right_y_middle=29
    self.prev_button_arrow_right_offset_border=4
    self.prev_button_rect_right_x_up=50-21
    self.prev_button_rect_right_y_up=54/2.-7.5
    self.prev_button_rect_right_x_width=64+16
    self.prev_button_rect_right_y_height=54/2.-7.5
 
 
    self.next_button_text="  NEXT    "
    self.next_button_text_x=980-50-21-23
    self.next_button_text_y=54/2.-7.5
    self.next_button_arrow_right_x=980-50+21
    self.next_button_arrow_right_y=4
    self.next_button_arrow_right_y_down=54
    self.next_button_arrow_right_y_middle=29
    self.next_button_arrow_right_offset_border=980-4
    self.next_button_rect_right_x_up=980-50-21-54+21
    self.next_button_rect_right_y_up=54/2.-7.5
    self.next_button_rect_right_x_width=64+16
    self.next_button_rect_right_y_height=54/2.-7.5
 
    self.select_level_pos_x=272+16
    self.select_level_pos_y=680-(680-552)+32+8
 
    self.left_tiny_snake_image_pos_x=16
    self.left_tiny_snake_image_pos_y=552
 
    self.right_tiny_snake_image_pos_x=980-(16+272)
    self.right_tiny_snake_image_pos_y=552
 
    self.levels_images_x=128
    self.levels_images_y=32+16+4
 
    self.tiny_snakes_left_images_index=0
    self.tiny_snakes_right_images_index=0
 
    self.level_name_selecting_color_index=0
 
    self.level_selecting_footer_color="Green"
 
    game_mainloop_control.from_level_selecting=True
    run=True
    while run :
      screen.fill((0))
      if game_mainloop_control.animate_next_level :
	# Animate level title text and image change.

	if game_mainloop_control.animate_level_title_font > 0 and game_mainloop_control.animate_level_title_lt :
	  # Make the level title text littler
	  game_mainloop_control.animate_level_title_font -= 2
	  self.change_level_animate_title(game_mainloop_control.animate_level_title_font)
	  self.change_level_selecting_animate_updating(False,game_mainloop_control.animate_level_title_font)

	elif game_mainloop_control.animate_level_title_font == 0 and game_mainloop_control.animate_level_title_lt :
	  # Change level title text.
          self.level_name_selecting=self.levels_names[self.level_name_index]
	  game_mainloop_control.animate_level_title_lt=False
	  game_mainloop_control.animate_level_title_gt=True

	elif game_mainloop_control.animate_level_title_font < 64 and game_mainloop_control.animate_level_title_gt :
	  # Make the level title text greater
	  game_mainloop_control.animate_level_title_font += 2
	  self.change_level_animate_title(game_mainloop_control.animate_level_title_font)
	  self.change_level_selecting_animate_updating(False,game_mainloop_control.animate_level_title_font)



	if game_mainloop_control.button_pressed == "Next"  :
	  if self.levels_images_x > 0-723 and game_mainloop_control.level_image_is_display :
	    # Slide level image to the left over the left border.
	    self.levels_images_x -= 24
	 
	  elif self.levels_images_x <= 0-723 and game_mainloop_control.level_image_is_display :
	    # Level image is hidden.
	    game_mainloop_control.level_image_is_display=False
	    self.levels_images_x=980
	 
	    # Update level image to display.
	    if self.level_tiny_images_index < 8 :
	      self.level_tiny_images_index += 1
	    if self.level_tiny_images_index == 8 :
	      self.level_tiny_images_index=0
	   
	  elif self.levels_images_x > 128 and not game_mainloop_control.level_image_is_display :
	    # Slide level image from the right border to center.
	    self.levels_images_x -= 24
	 
	  else :
	    # Level image is centered.
	    self.change_level_animate_end_update()
	 
	 
	if game_mainloop_control.button_pressed == "Prev"  :
	  if self.levels_images_x >= 128 and self.levels_images_x < 980 and game_mainloop_control.level_image_is_display :
	    # Slide level image to the left over the left border.
	    self.levels_images_x += 24
	 
	  elif self.levels_images_x > 980 and game_mainloop_control.level_image_is_display :
	 
	    # Level image is hidden.
	    game_mainloop_control.level_image_is_display=False
	    self.levels_images_x=0-723
	 
	    # Update level image to display.
	    if self.level_tiny_images_index > 0 :
	      self.level_tiny_images_index -= 1
	    else :
	      self.level_tiny_images_index=7
	   
	  elif self.levels_images_x < 128 and not game_mainloop_control.level_image_is_display :
	    # Slide level image from the right border to center.
	    self.levels_images_x += 24
	 
	  else :
	    # Level image is centered.
	    self.change_level_animate_end_update()

      # Blit level image
      screen.blit(self.levels_tiny_images[self.level_tiny_images_index],(self.levels_images_x,self.levels_images_y))
   
   
      # Blit previous button
      pygame.draw.polygon(screen,self.prev_button_color,[(self.prev_button_arrow_right_x,self.prev_button_arrow_right_offset_border),(self.prev_button_arrow_right_x,self.prev_button_arrow_right_y_down),(self.prev_button_arrow_right_offset_border,self.prev_button_arrow_right_y_middle)],0)
      pygame.draw.rect(screen,self.prev_button_color,((self.prev_button_rect_right_x_up,self.prev_button_rect_right_y_up), (self.prev_button_rect_right_x_width, self.prev_button_rect_right_y_height)),0)
      screen.blit(font_buttons.render(self.prev_button_text,True,self.prev_button_text_color),(self.prev_button_text_x,self.prev_button_text_y))
   
      # Blit next button
      pygame.draw.polygon(screen,self.next_button_color,[(self.next_button_arrow_right_x,self.next_button_arrow_right_y),(self.next_button_arrow_right_x,self.next_button_arrow_right_y_down),(self.next_button_arrow_right_offset_border,self.next_button_arrow_right_y_middle)],0)
      pygame.draw.rect(screen,self.next_button_color,((self.next_button_rect_right_x_up,self.next_button_rect_right_y_up), (self.next_button_rect_right_x_width, self.next_button_rect_right_y_height)),0)
      screen.blit(font_buttons.render(self.next_button_text,True,(0,0,0)),(self.next_button_text_x,self.next_button_text_y))
   
      screen.blit(self.font_select_level_title.render(self.level_name_selecting,True,self.blink_choice_color[self.level_name_selecting_color_index]),((980/2.)-(self.font_select_level_title.size(self.level_name_selecting)[0]/2.),2))
   
      # Blit footer images and imaes
      screen.blit(self.tiny_snakes_left_images[self.tiny_snakes_left_images_index],(self.left_tiny_snake_image_pos_x,self.left_tiny_snake_image_pos_y))
      #screen.blit(self.font_game_level_play.render("[ <-prev ] Level to play  [ next -> ]",True,(0,255,0,255)),(272+64,680-(680-552)+16))
      screen.blit(self.font_select_level_message.render(self.select_level_string, True,self.blink_choice_color[self.level_name_selecting_color_index]),(self.select_level_pos_x,self.select_level_pos_y))
      screen.blit(self.font_select_level_message.render(self.select_highscore_string,True,self.blink_choice_color[self.level_name_selecting_color_index]),(self.select_level_pos_x,self.select_level_pos_y+32))
      screen.blit(self.tiny_snakes_right_images[self.tiny_snakes_right_images_index],(self.right_tiny_snake_image_pos_x,self.right_tiny_snake_image_pos_y))
   
      for event in pygame.event.get() :
	if event.type == QUIT :
	  exit()
	if event.type == MOUSEMOTION :
	  if event.pos[0] >= 4 and event.pos[0] <= 4+64+16 and event.pos[1] <= 54 and event.pos[1] >= 4 :
	    if self.level_name_index % 2 == 0 :
	     self.prev_button_color=(255,0,0)
	    else :
	     self.prev_button_color=(0,255,0)
	   
	  elif event.pos[0] >= 980-50-21-54+21 and event.pos[0] <= 980-50-21-54+21+4+64+16 and event.pos[1] <= 54 and event.pos[1] >= 4 :
	    if self.level_name_index % 2 == 0 :
	     self.next_button_color=(255,0,0)
	    else :
	     self.next_button_color=(0,255,0)
	  else :
	    if self.level_name_index % 2 == 0 :
	      self.prev_button_color=(0,255,0)
	      self.next_button_color=(0,255,0)
	    else :
	      self.prev_button_color=(255,0,0)
	      self.next_button_color=(255,0,0)
	   
	elif event.type == MOUSEBUTTONDOWN :
	  if event.pos[0] >= 980-50-21-54+21 and event.pos[0] <= 980-50-21-54+21+4+64+16 and event.pos[1] <= 54 and event.pos[1] >= 4 :
	    if not game_mainloop_control.is_animating :
	      self.choice_prev_level()

	  elif event.pos[0] >= 4 and event.pos[0] <= 4+64+16 and event.pos[1] <= 54 and event.pos[1] >= 4 :
	    if not game_mainloop_control.is_animating :
	      self.choice_next_level()
	 
   
	elif event.type == KEYDOWN :
	  if event.key == K_RIGHT or event.key == K_KP6 :
	    if not game_mainloop_control.is_animating :
	      self.choice_prev_level()
	  elif event.key == K_LEFT or event.key == K_KP4 :
	    if not game_mainloop_control.is_animating :
	      self.choice_next_level()
          elif event.key == K_RETURN :
	    if not game_mainloop_control.is_animating :
	      run=False
	      self.init_level(self.level_name_index)
	      self.playing_level()
	  elif event.key == K_SPACE :
	    run=False
	    self.show_highscore(self.level_name_index) 
	  elif event.key == K_ESCAPE :
	    run=False
	    game_mainloop.start_game_animation()
	   
      sleep(game_mainloop_control.choose_level_sleep)
      pygame.display.update()


  def choice_next_level(self) :
 
    game_mainloop_control.is_animating=True
    animation_sounds.play_rattle_select_level()
    if self.level_name_index > 0 :
      self.level_name_index -= 1
   
    else :
      self.level_name_index=7
 
    if self.level_name_index % 2 == 0 :
      self.level_selecting_footer_color="Green"
    else :
      self.level_selecting_footer_color="Red"
   
    game_mainloop_control.button_pressed="Prev"
 
    game_mainloop_control.animate_level_title_lt=True
    game_mainloop_control.choose_level_sleep=0.025
    game_mainloop_control.animate_next_level=True

  def choice_prev_level(self) :
    game_mainloop_control.is_animating=True
    animation_sounds.play_rattle_select_level()
    if self.level_name_index < 8 :
      self.level_name_index += 1
 
    if self.level_name_index == 8 :
      self.level_name_index=0
 
    if self.level_name_index % 2 == 0 :
      self.level_selecting_footer_color="Green"
    else :
      self.level_selecting_footer_color="Red"
   
    game_mainloop_control.button_pressed="Next"
    game_mainloop_control.animate_level_title_lt=True
    game_mainloop_control.choose_level_sleep=0.025
    game_mainloop_control.animate_next_level=True

  def change_level_animate_end_update(self) :
    game_mainloop_control.level_image_is_display=True
    game_mainloop_control.button_pressed=False
    game_mainloop_control.animate_next_level=False
    game_mainloop_control.level_image_is_display=True
    game_mainloop_control.is_animating=False
 
    game_mainloop_control.choose_level_sleep=0.0

    if self.level_tiny_images_index % 2 == 0 :
      self.change_level_selecting_animate_updating("Green",game_mainloop_control.animate_level_title_font)
    else :
      self.change_level_selecting_animate_updating("Red",game_mainloop_control.animate_level_title_font)

    self.levels_images_x=128

  def change_level_animate_title(self,i) :
    self.font_select_level_title=pygame.font.SysFont("San-Serif", i, True, False)

  def change_level_selecting_animate_updating(self,end_color,timer) :
 
    if timer % 16 == 0 :
      if self.level_name_selecting_color_index == 0 and not end_color :
	self.level_name_selecting_color_index=1
	self.level_name_selecting_color_index=1
	self.tiny_snakes_left_images_index=1
	self.tiny_snakes_right_images_index=1
	self.prev_button_color=(255,0,0)
	self.next_button_color=(255,0,0)

      elif self.level_name_selecting_color_index == 1 and not end_color :
	self.level_name_selecting_color_index=0
	self.tiny_snakes_left_images_index=0
	self.tiny_snakes_right_images_index=0
	self.prev_button_color=(0,255,0)
	self.next_button_color=(0,255,0)
   
      elif self.level_name_selecting_color_index == 0 and end_color == "Red" :
	self.level_name_selecting_color_index=1
	self.tiny_snakes_left_images_index=1
	self.tiny_snakes_right_images_index=1
	self.prev_button_color=(255,0,0)
	self.next_button_color=(255,0,0)
   
      elif self.level_name_selecting_color_index == 1 and end_color == "Green" :
	self.level_name_selecting_color_index=0
	self.tiny_snakes_left_images_index=0
	self.tiny_snakes_right_images_index=0
	self.prev_button_color=(0,255,0)
	self.next_button_color=(0,255,0)
   
  def start_game_animation(self) :
 
    global animation_sounds
 
    pygame.display.set_caption("SnakeByte")
    pygame.display.set_icon(self.iconfy_icon)
 
    self.blink_choice_color=[(0,255,0),(255,0,0)]
    self.blink_choice_color_modulo=1
    screen=pygame.display.set_mode((980, 680),0,32)
 
 
 
 
 
    self.font_game_title=pygame.font.SysFont("San-Serif", 96, True, False)
 
 
    self.intro_animation_images=listdir(self.intro_animation_dir)
    self.intro_animation_images.sort()
 
    sleeping_image_slide=0.01
    sleeping_title_slide=0.001
    sleeping=sleeping_image_slide
 
    title_slide_to_front=64
    title_text_x=980-self.title_font_size
    title_text_y=32
 
 
    if not game_mainloop_control.start_side_static :


      animation_sounds=Animations_sounds()
      animation_sounds.set_intro_music_start()
      animation_sounds.play_rattle_start_animation()

     
    elif game_mainloop_control.start_side_static :

      if not game_mainloop_control.from_level_selecting :
	pygame.mixer.music.stop()
        animation_sounds=Animations_sounds()
        animation_sounds.set_intro_music_start()
        pygame.mixer.music.set_volume(0.5)


      sleeping=0.75
      self.level_anim_x=16
      title_text_x=276
      self.title_font_size=128
      self.font_game_title=pygame.font.SysFont("San-Serif", self.title_font_size, True, False)
   
    intro_animation_image_index=0
 
 
 
 
 
 
 
 
 
    timer=0.0
    run=True
 
 
    bool_bounce_effect_back=False
    bool_bounce_effect_forward=False
    while run :
      screen.fill((0))
   

      if ( intro_animation_image_index < 62 ) 	and not game_mainloop_control.start_side_static :
	# Setting the image for the snake animation.
        image_intro_animation=pygame.image.load(self.intro_animation_dir+self.intro_animation_images[intro_animation_image_index])
      elif game_mainloop_control.start_side_static :
	# Snake animation is completed.
	image_intro_animation=pygame.image.load(self.intro_animation_dir+"intro_anim_62.png")
     
     
      screen.blit(image_intro_animation,(0,32))
   
      if self.show_game_title and self.title_font_size < 128 :
	self.font_game_title=pygame.font.SysFont("San-Serif", self.title_font_size, True, False)
	screen.blit(self.font_game_title.render("SnakeByte", True, (0,255,0,255)),(title_text_x,title_text_y))
	title_slide_to_front = title_slide_to_front + 10 # The title text animating: it comes from backward to the center.
	self.title_font_size += 2                        # The title text animating: the title text become greater.
	title_text_x=980-title_slide_to_front            # Setting text position.
   
      elif self.show_game_title and self.title_font_size == 128 and not game_mainloop_control.start_side_static and not self.show_level_choice:
	# Title text animaing is completed.
	self.font_game_title=pygame.font.SysFont("San-Serif", self.title_font_size, True, False)
	title_text_x=980-title_slide_to_front
	screen.blit(self.font_game_title.render("SnakeByte", True, (0,255,0,255)),(title_text_x,title_text_y))
   

      if self.show_game_title and not self.show_level_choice  :
        if self.level_anim_x > 16 :
          screen.blit(self.tiny_snake_left_green_image,(self.level_anim_x,self.level_anim_y))
          screen.blit(self.tiny_snake_right_green_image,(980-(self.level_anim_x+272),self.level_anim_y)) # 272 pixels is the width of the tiny snake image.
          self.level_anim_x -= 9
          if self.level_anim_x <= 16 :
	    # Tiny snakes images animation is completed.
	    self.show_level_choice=True
	    self.level_anim_x=16
          pygame.display.update()
          continue

      elif self.show_level_choice or game_mainloop_control.start_side_static :
	game_mainloop_control.is_animation_intro_running=False
	# End of all animations.
	# Making the tiny snakes and the select level text blinking:
	if self.blink_choice_color_modulo == 3 :
	  self.blink_choice_color_modulo=1

	self.font_game_title=pygame.font.SysFont("San-Serif", self.title_font_size, True, False)
	title_text_x=276
	screen.blit(self.font_game_title.render("SnakeByte", True, self.blink_choice_color[self.blink_choice_color_modulo%2]),(title_text_x,title_text_y))

	screen.blit(self.tiny_snakes_left_images[self.blink_choice_color_modulo%2],(16,self.level_anim_y))
        screen.blit(self.font_select_level_message.render(self.goto_select_level_strings, True,self.blink_choice_color[self.blink_choice_color_modulo%2]),(272+24,680-(680-self.level_anim_y)+32+8))
        screen.blit(self.tiny_snakes_right_images[self.blink_choice_color_modulo%2],(980-(self.level_anim_x+272),self.level_anim_y))
        self.blink_choice_color_modulo += 1
     
      for event in pygame.event.get() :
	if event.type == QUIT :
	  exit()
        if event.type == KEYDOWN :
	  if event.key == K_RETURN :
	    if not game_mainloop_control.is_animation_intro_running :
	      game_mainloop_control.start_side_static=True
	      run=False
              self.show_level_presentation()
	 
   
      if (intro_animation_image_index  < 62 and not bool_bounce_effect_back and not bool_bounce_effect_forward ) :
	# Snake image comes from the deep to the front progessiv.
	# by update the image index.
	intro_animation_image_index += 1
   
   
      elif intro_animation_image_index == 62 and not self.show_level_choice and not bool_bounce_effect_back 	and not bool_bounce_effect_forward :
	# Snake image is as front of the display.
	# We swicth to bounce the snake back.
	bool_bounce_effect_back=True
	intro_animation_image_index=62
	sleeping=0.03
      elif intro_animation_image_index > 48 and not self.show_level_choice and bool_bounce_effect_back and not bool_bounce_effect_forward :
	# Snake image back bouncing.
	intro_animation_image_index -= 1
      elif intro_animation_image_index == 48 and not self.show_level_choice and bool_bounce_effect_back and not bool_bounce_effect_forward :
	# Snake image is in the middle of the display.
	# We switch to bounce the snake forward.
	bool_bounce_effect_forward=True
	bool_bounce_effect_back=False
      elif intro_animation_image_index < 62 and not self.show_level_choice and not bool_bounce_effect_back and bool_bounce_effect_forward :
	# Snake image forward bouncing.
	intro_animation_image_index += 1
      elif intro_animation_image_index == 62 and not self.show_level_choice and not bool_bounce_effect_back and bool_bounce_effect_forward :
	# Snake image is as front of the display.
	# End of the snake animation.
	bool_bounce_effect_forward=False
	self.show_game_title=True
	sleeping=sleeping_title_slide
	pygame.mixer.music.set_volume(0.5)
      elif self.show_level_choice :
	sleeping=0.75

      sleep(sleeping)
      timer += sleeping
      pygame.display.update() 
 

  def init_level(self,level_n) :
    global level,phantoms_entities,snake,playground,game_control,game_sound,game_text,highscore,win_bool
 
    self.level=level_n
    game_mainloop_control.from_level_selecting=False
 
    level=Level(self.levels_snale_start_orientation[level_n],self.levels_files_dir+self.levels_files[level_n])
 
    win_bool=False

    phantoms_entities=level.compute_phantoms()
 
    snake=Snake(level.get_start_snake_head_position(),level.compute_level_data('snake'))

    playground=Playground(level.compute_level_data('apples'),level.compute_level_data('barriers'),level.compute_level_data('exit'),self.levels_snake_colors[level_n],self.levels_background_colors[level_n])   
    playground.losing_compute_down_gradient()
    playground.barriers_color_inversing()
    playground.phantoms_color_inversing()
 
    game_control=Game_control(len(level.compute_level_data('apples')))  
 
    level.compute_barriers_collide_rect_list()
    level.compute_eat_apple_collide_rect_list()
    level.compute_phantom_collide_rect_list()
    level.compute_exit_collide_rect_list()
    game_sound=Game_sound()

    game_sound.background_music_start()

    game_clock=pygame.time.Clock()
    game_clock.tick(75)
 
    highscore=Highscores()
    game_text=Game_text()


  def playing_level(self) :
    global screen,win_bool
 
    pygame.display.set_caption("SnakeByte")
    pygame.display.set_icon(self.iconfy_icon)
 
    screen=pygame.display.set_mode(level.get_resolution(),0,32)
 
    i=0
 
    ret=True
 
    i=0
    run=True
    win_end_game_anim_counter=0
    while run :
   
      screen.fill(playground.background_color)
   
      if game_control.animate_start_game :
	playground.set_snake_color_start_animation(i)
        playground.draw_playground()
        pygame.display.update()
        i += 1
	if  ( i == 16) :
	  game_control.animate_start_game=False
	else :
	  sleep(0.25)
	continue
 
   
      if game_control.animation_losing :
	if playground.losing_bink_time :
	  playground.losing_blink_snake()
	else :
	  snake.snake_speed=snake.snake_speed*1.1

	  ret=playground.losing_change_snake_color_gradient()
	if ( not ret) :
	  playground.draw_playground()
	  playground.losing_bink_time=False
	  game_control.game_over=True
	  game_control.animation_losing=False
	  run=False
	  break
   
	   
	 
   
      if game_control.animate_phantom and not game_control.animation_exit_open_running :
	playground.phamtoms_forward()
	level.compute_phantom_collide_rect_list()
     
   
      if not game_control.snake_stop and not game_control.animation_blocking and not game_control.animation_slide and not game_control.animation_losing and not game_control.animation_exit_open_running  :
	snake.forward()
	pass

   

      playground.draw_playground()
   
   
   
      if not game_control.exit_closed  :
	win_bool=playground.check_snake_go_exit()
	if win_bool :
	  win_end_game_anim_counter += 1
	  if win_end_game_anim_counter == 3 :
	    game_control.snake_player_win=True
	    game_control.animation_blocking=True
	    game_control.animation_losing=True
            game_sound.losing_sound_play()
	    game_control.animate_phantom =  False
   
      if not game_control.animation_losing :
	# Comment following line to not lose by hit the phantoms.
	game_control.animation_losing=playground.check_phantom_colliding()
	if game_control.animation_losing :
	  game_control.snake_lifes -= 1
	  game_control.animate_phantom =  False
   
      if not game_control.animation_losing  :
	# Comment following line to not lose by hit the walls.
	game_control.animation_losing=playground.check_barriers_colliding()
	pass
	if game_control.animation_losing :
	  game_control.snake_lifes -= 1
	  game_control.animate_phantom =  False
	pass
   
      if not game_control.all_apples_eat  :
	game_control.all_apples_eat=playground.check_eat_apple_colliding()
   
      if game_control.all_apples_eat and not game_control.animation_exit_open_running and game_control.exit_closed  :
	# Open exit animation starting.
	playground.start_animation_exit_open()


      #Event getting loop with conditionnal structure to handle
      for event in pygame.event.get() :
	 
	if event.type == QUIT :
	  exit()

	if event.type == USEREVENT and event.code == "opening_animation" :
	  if game_control.exit_closed :
	    playground.set_animation_exit_open_next()
	 
	    next_step_anim_event=pygame.event.Event(USEREVENT, {'code' : "opening_animation"} )
	    pygame.event.post(next_step_anim_event)
	 
	    continue


	if event.type == KEYDOWN :
	  if game_control.animation_losing :
	    continue


	  if event.key == K_RIGHT :
	    if not game_control.snake_stop :
	      if (snake.anim_turn_length <= snake.length) :
		game_control.set_animation_blocking_on()
		if snake.anim_turn_length == 1 :
		  game_control.set_animation_turning_right_on()
		  game_sound.turn_right_sound_play()
		if ( not game_control.animation_turning_left and not game_control.animation_slide ) :
		  snake.turn_right(snake.anim_turn_length)
	
		  playground.draw_playground()
		  next_step_anim_event=pygame.event.Event(KEYDOWN, {'key' : K_RIGHT} )
		  pygame.event.post(next_step_anim_event)
		  continue
	   
	      else :
		snake.anim_turn_length=1
		game_control.set_animation_blocking_off()
		continue
	   
	 
	   
	  elif event.key == K_LEFT :
	    if not game_control.snake_stop :
	      if (snake.anim_turn_length <= snake.length) :
		game_control.set_animation_blocking_on()
		if snake.anim_turn_length == 1 :
		  game_control.set_animation_turning_left_on()
		  game_sound.turn_left_sound_play()
		if ( not game_control.animation_turning_right and not game_control.animation_slide ) :
		  snake.turn_left(snake.anim_turn_length)
   
		  playground.draw_playground()
		  next_step_anim_event=pygame.event.Event(KEYDOWN, {'key' : K_LEFT} )
		  pygame.event.post(next_step_anim_event)
		  continue
	      else :
		snake.anim_turn_length=1
		game_control.set_animation_blocking_off()
		continue
	 

	  elif event.key == K_q or event.key == K_a :
	    if not game_control.snake_stop :
	      game_control.set_animation_sliding_on()

	      snake.anim_slide_left()
	      game_sound.turn_slide_sound_play()

	      playground.draw_playground()
	      game_control.set_animation_sliding_off()
	 
	      continue
	 
	  elif event.key == K_d :
	    if not game_control.snake_stop :
	      game_control.set_animation_sliding_on()
	   
	      snake.anim_slide_right() # Slide the snake to the right from one field in the actual orientation.
	      game_sound.turn_slide_sound_play()

	      playground.draw_playground()
	      game_control.set_animation_sliding_off()

	      continue
	 
	  elif event.key == K_z or event.key == K_w :
	    if not game_control.snake_stop :
	      game_control.snake_stop=True
	      playground.draw_playground()
	      sleep(snake.snake_speed)
	      pygame.display.update()
	      continue
	    else :
	      game_control.snake_stop=False
	      continue

	  elif event.key == K_ESCAPE :
	    run=False
	    self.start_game_animation()
	 

      playground.draw_playground()
      sleep(snake.snake_speed)
 
      pygame.display.update()
 
    if game_control.snake_lifes == 0 or win_bool :
      self.game_over_display()
    else :
      self.lose_a_life_display()
   

  def lose_a_life_display(self) :
 
    global snake, phantoms_entities
 
    run=True
    while run :
   
      screen.fill(playground.background_color)
      playground.draw_playground()
   
      screen.blit(game_text.little_font.render("You lose a life, try again !",True,(255,255,255,255)),(((980/2)-(game_text.little_font.size("You lose a life, try again !")[0]/2)), ((680/2)-(game_text.little_font.size("You lose a life, try again !")[1]/2)) ) )
      screen.blit(game_text.little_font.render("Life points: %d/10" % game_control.snake_lifes,True,(255,255,255,255)),( ((980/2)-(game_text.little_font.size("Life points: %d/10" % game_control.snake_lifes)[0]/2)), ((680/2)-(game_text.little_font.size("Life points: %d/10" % game_control.snake_lifes)[1]/2)+64) ) )
      pygame.display.update()
      sleep(0.75)
   
      screen.blit(game_text.little_font.render("You lose a life, try again !",True,playground.snake_color_back_up),(((980/2)-(game_text.little_font.size("You lose a life, try again !")[0]/2)), ((680/2)-(game_text.little_font.size("You lose a life, try again !")[1]/2)) ) )
      screen.blit(game_text.little_font.render("Life points: %d/10" % game_control.snake_lifes,True,playground.snake_color_back_up),( ((980/2)-(game_text.little_font.size("Life points: %d/10" % game_control.snake_lifes)[0]/2)), ((680/2)-(game_text.little_font.size("Life points: %d/10" % game_control.snake_lifes)[1]/2)+64) ) )
      pygame.display.update()
      sleep(0.75)
   
      screen.blit(game_text.little_font.render("You lose a life, try again !",True,(255,255,255,255)),(((980/2)-(game_text.little_font.size("You lose a life, try again !")[0]/2)), ((680/2)-(game_text.little_font.size("You lose a life, try again !")[1]/2)) ) )
      screen.blit(game_text.little_font.render("Life points: %d/10" % game_control.snake_lifes,True,(255,255,255,255)),( ((980/2)-(game_text.little_font.size("Life points: %d/10" % game_control.snake_lifes)[0]/2)), ((680/2)-(game_text.little_font.size("Life points: %d/10" % game_control.snake_lifes)[1]/2)+64) ) )
      pygame.display.update()
      sleep(0.75)
   
      screen.blit(game_text.little_font.render("You lose a life, try again !",True,playground.snake_color_back_up),(((980/2)-(game_text.little_font.size("You lose a life, try again !")[0]/2)), ((680/2)-(game_text.little_font.size("You lose a life, try again !")[1]/2)) ) )
      screen.blit(game_text.little_font.render("Life points: %d/10" % game_control.snake_lifes,True,playground.snake_color_back_up),( ((980/2)-(game_text.little_font.size("Life points: %d/10" % game_control.snake_lifes)[0]/2)), ((680/2)-(game_text.little_font.size("Life points: %d/10" % game_control.snake_lifes)[1]/2)+64) ) )
      pygame.display.update()
      sleep(0.75)
   
      screen.blit(game_text.little_font.render("You lose a life, try again !",True,(255,255,255,255)),(((980/2)-(game_text.little_font.size("You lose a life, try again !")[0]/2)), ((680/2)-(game_text.little_font.size("You lose a life, try again !")[1]/2)) ) )
      screen.blit(game_text.little_font.render("Life points: %d/10" % game_control.snake_lifes,True,(255,255,255,255)),( ((980/2)-(game_text.little_font.size("Life points: %d/10" % game_control.snake_lifes)[0]/2)), ((680/2)-(game_text.little_font.size("Life points: %d/10" % game_control.snake_lifes)[1]/2)+64) ) )
      pygame.display.update()
      sleep(1.5)
   
      sleep(snake.snake_speed)
      pygame.display.update()
   
      pygame.event.clear()
   
      break
 
 
    # Reset losing blinking settings.
    playground.losing_bink_time=16
 
    # Reset game control variable.
    game_control.animate_phantom=True
    game_control.animate_start_game=True
    game_control.animation_blocking=False
    game_control.animation_losing=False
    game_control.animation_slide=False
    game_control.snake_stop=False
 
    # Reset snake position.
    snake=Snake(level.get_start_snake_head_position(),level.compute_level_data('snake'))
 
    # Reset phantoms position.
    phantoms_entities=level.compute_phantoms()
 
    self.playing_level()
 
 
   
   
 

  def game_over_display(self) :
 
    run=True
    while run :
   
      if game_control.animation_losing :
	if playground.losing_bink_time :
	  playground.losing_blink_snake()
	else :
	  snake.snake_speed=snake.snake_speed*1.1

	  ret=playground.losing_change_snake_color_gradient()
	if ( not ret) :
	  playground.draw_playground()
	  playground.losing_bink_time=False
	  game_control.game_over=True
	  game_control.animation_losing=False
	  run=False
	  break
   
      screen.fill(playground.background_color)
      playground.draw_playground()
   
      if game_control.game_over :
	percent=100./game_control.apples_total
	self.percent_apples_eat=str(round(game_control.apple_counter*percent,2))
	percent_apples_eat_int=self.percent_apples_eat[0:self.percent_apples_eat.index(".")]
	percent_apples_eat_float=self.percent_apples_eat[self.percent_apples_eat.index(".")+1::]+str((2-len(self.percent_apples_eat[self.percent_apples_eat.index(".")+1::]))*'0')
	self.percent_apples_eat_string=percent_apples_eat_int.zfill(3)+"."+percent_apples_eat_float

	if not game_control.snake_player_win :
	  if game_control.game_over_text_display :
	    screen.blit(game_text.little_font.render("Apples eat: %s / %s (%s %%)" % (game_control.apple_counter,game_control.apples_total,self.percent_apples_eat_string ),True,(255,255,255,255)),(((980/2)-(game_text.little_font.size("Apples eat: %s / %s (%s %%)" % (game_control.apple_counter,game_control.apples_total,self.percent_apples_eat_string))[0]/2)-64), ((680/2)-(game_text.little_font.size("Apples eat: %s / %s (%s %%)" % (game_control.apple_counter,game_control.apples_total,self.percent_apples_eat_string))[1]/2)) ) )
	    screen.blit(game_text.little_font.render("Registering score ?",True,(255,255,255,255)),( ((980/2)-(game_text.little_font.size("Registering score ?")[0]/2)), ((680/2)-(game_text.little_font.size("Registering score ?")[1]/2)+64) ) )
	    if game_control.registering_score_answers == "NO" :
	      screen.blit(game_text.little_font.render("YES",True,(255,255,255,255)),( ((980/2)-(game_text.little_font.size("YES")[0]/2)-(game_text.little_font.size("YES")[0]/2)*2), ((680/2)-(game_text.little_font.size("YES")[1]/2)+128 ) ) )
	      screen.blit(game_text.little_font.render("NO",True,playground.snake_color_back_up),( ((980/2)-(game_text.little_font.size("NO")[0]/2)+(game_text.little_font.size("NO")[0]/2)*2), ((680/2)-(game_text.little_font.size("NO")[1]/2)+128 ) ) )
	    elif game_control.registering_score_answers == "YES" :
	      screen.blit(game_text.little_font.render("YES",True,playground.snake_color_back_up),( ((980/2)-(game_text.little_font.size("YES")[0]/2)-(game_text.little_font.size("YES")[0]/2)*2), ((680/2)-(game_text.little_font.size("YES")[1]/2)+128 ) ) )
	      screen.blit(game_text.little_font.render("NO",True,(255,255,255,255)),( ((980/2)-(game_text.little_font.size("NO")[0]/2)+(game_text.little_font.size("NO")[0]/2)*2), ((680/2)-(game_text.little_font.size("NO")[1]/2)+128 ) ) )
            pygame.display.update()

	  elif not game_control.game_over_text_display :
	    screen.blit(game_text.big_font.render("GAME OVER", True, (255,255,255,255)), (((980/2)-(game_text.big_font.size("GAME OVER")[0]/2)), ((680/2)-(game_text.big_font.size("GAME OVER")[1]/2))) )
	    pygame.display.update()
	    sleep(0.75)
	    screen.blit(game_text.big_font.render("GAME OVER", True, playground.snake_color_back_up), (((980/2)-(game_text.big_font.size("GAME OVER")[0]/2)), ((680/2)-(game_text.big_font.size("GAME OVER")[1]/2))) )
	    pygame.display.update()
	    sleep(0.75)
	    screen.blit(game_text.big_font.render("GAME OVER", True, (255,255,255,255)), (((980/2)-(game_text.big_font.size("GAME OVER")[0]/2)), ((680/2)-(game_text.big_font.size("GAME OVER")[1]/2))) )
	    pygame.display.update()
	    sleep(0.75)
	    screen.blit(game_text.big_font.render("GAME OVER", True, playground.snake_color_back_up), (((980/2)-(game_text.big_font.size("GAME OVER")[0]/2)), ((680/2)-(game_text.big_font.size("GAME OVER")[1]/2))) )
	    pygame.display.update()
	    sleep(0.75)
	    screen.blit(game_text.big_font.render("GAME OVER", True, (255,255,255,255)), (((980/2)-(game_text.big_font.size("GAME OVER")[0]/2)), ((680/2)-(game_text.big_font.size("GAME OVER")[1]/2))) )
	    pygame.display.update()
	    sleep(0.75)
	    snake.snake_speed=0.0
	    game_control.game_over_text_display=True
	else :
	  if game_control.game_over_text_display :
	    screen.blit(game_text.little_font.render("Apples eat: %s / %s (%s %%)" % (game_control.apple_counter,game_control.apples_total,percent_apples_eat_int.zfill(3)+"."+percent_apples_eat_float ),True,(255,255,255,255)),( ((980/2)-(game_text.little_font.size("Apples eat: %s / %s (%s %%)" % (game_control.apple_counter,game_control.apples_total,str(round(game_control.apple_counter*percent,2)).zfill(3) ))[0]/2)-64), ((680/2)-(game_text.little_font.size("Apples eat: %s / %s (%s %%)" % (game_control.apple_counter,game_control.apples_total,str(round(game_control.apple_counter*percent,2)).zfill(3) ))[1]/2)) ) )
	    screen.blit(game_text.little_font.render("Registering score ?",True,(255,255,255,255)),( ((980/2)-(game_text.little_font.size("Registering score ?")[0]/2)), ((680/2)-(game_text.little_font.size("Registering score ?")[1]/2)+64) ) )
	    if game_control.registering_score_answers == "NO" :
	      screen.blit(game_text.little_font.render("YES",True,(255,255,255,255)),( ((980/2)-(game_text.little_font.size("YES")[0]/2)-(game_text.little_font.size("YES")[0]/2)*2), ((680/2)-(game_text.little_font.size("YES")[1]/2)+128 ) ) )
	      screen.blit(game_text.little_font.render("NO",True,playground.snake_color_back_up),( ((980/2)-(game_text.little_font.size("NO")[0]/2)+(game_text.little_font.size("NO")[0]/2)*2), ((680/2)-(game_text.little_font.size("NO")[1]/2)+128 ) ) )
	    elif game_control.registering_score_answers == "YES" :
	      screen.blit(game_text.little_font.render("YES",True,playground.snake_color_back_up),( ((980/2)-(game_text.little_font.size("YES")[0]/2)-(game_text.little_font.size("YES")[0]/2)*2), ((680/2)-(game_text.little_font.size("YES")[1]/2)+128 ) ) )
	      screen.blit(game_text.little_font.render("NO",True,(255,255,255,255)),( ((980/2)-(game_text.little_font.size("NO")[0]/2)+(game_text.little_font.size("NO")[0]/2)*2), ((680/2)-(game_text.little_font.size("NO")[1]/2)+128 ) ) )
            pygame.display.update()

	  elif not game_control.game_over_text_display :
	    screen.blit(game_text.big_font.render("YOU WIN", True, (255,255,255,255)), (((980/2)-(game_text.big_font.size("YOU WIN")[0]/2)), ((680/2)-(game_text.big_font.size("YOU WIN")[1]/2))) )
	    pygame.display.update()
	    sleep(0.75)
	    screen.blit(game_text.big_font.render("YOU WIN", True, playground.snake_color_back_up), (((980/2)-(game_text.big_font.size("YOU WIN")[0]/2)), ((680/2)-(game_text.big_font.size("YOU WIN")[1]/2))) )
	    pygame.display.update()
	    sleep(0.75)
	    screen.blit(game_text.big_font.render("YOU WIN", True, (255,255,255,255)), (((980/2)-(game_text.big_font.size("YOU WIN")[0]/2)), ((680/2)-(game_text.big_font.size("YOU WIN")[1]/2))) )
	    pygame.display.update()
	    sleep(0.75)
	    screen.blit(game_text.big_font.render("YOU WIN", True, playground.snake_color_back_up), (((980/2)-(game_text.big_font.size("YOU WIN")[0]/2)), ((680/2)-(game_text.big_font.size("YOU WIN")[1]/2))) )
	    pygame.display.update()
	    sleep(0.75)
	    screen.blit(game_text.big_font.render("YOU WIN", True, (255,255,255,255)), (((980/2)-(game_text.big_font.size("YOU WIN")[0]/2)), ((680/2)-(game_text.big_font.size("YOU WIN")[1]/2))) )
	    pygame.display.update()
	    sleep(0.75)
	    snake.snake_speed=0.0
	    game_control.game_over_text_display=True

      for event in pygame.event.get() :
	   
	  if event.type == QUIT :
	    exit()

	  if event.type == KEYDOWN :
	      if event.key == K_RIGHT :
	   

		if game_control.game_over_text_display :
		  if game_control.registering_score_answers == "NO" :
		    game_control.registering_score_answers="YES"
		  else :
		    game_control.registering_score_answers="NO"
	   

	      elif event.key == K_LEFT :
	 
		if game_control.game_over_text_display :
		  if game_control.registering_score_answers == "NO" :
		    game_control.registering_score_answers="YES"
		  else :
		    game_control.registering_score_answers="NO"
	   
	      elif event.key == K_RETURN :
		if game_control.registering_score_answers == "YES" :
		  self.enter_username()
		elif game_control.registering_score_answers == "NO" :
		  run=False
	          game_mainloop.start_game_animation()
	
      sleep(snake.snake_speed)
      pygame.display.update()
   
  def enter_username(self) :
    global screen
    run=True
    self.username_store=[]
    self.username=""
    letters_display="A"
    letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Y","X","Z"]
    letters_index=0
 
    while run :
      screen.fill(playground.background_color)
      playground.draw_playground()
      screen.blit(game_text.little_font.render("Enter your name: ",True,(255,255,255,255)),( ((980/2)-(game_text.little_font.size("Enter your name: ")[0]/2)-64), ((680/2)-(game_text.little_font.size(("Enter your name: "))[1]/2)) ) )
      screen.blit(game_text.little_font.render("%s" % (self.username+letters_display ),True,(255,255,255,255)),( ((980/2)-(game_text.little_font.size("Enter your name: ")[0]/2-(game_text.little_font.size("Enter your name: ")[0]/4))-128), ((680/2)-(game_text.little_font.size(("Enter your name: "))[1]/2)+64) ) )

      for event in pygame.event.get() :
	   
	  if event.type == QUIT :
	    exit()
	  if event.type == KEYDOWN :
	    if event.key == K_UP :
	      if letters_index > 0 :
	        letters_index -= 1
	      else :
		letters_index=25
	      letters_display=letters[letters_index]
	    elif event.key == K_DOWN :
	      if letters_index < 25 :
	        letters_index += 1
	      else :
		letters_index=0
              letters_display=letters[letters_index]
            elif event.key == K_RIGHT :
	      if len(self.username) < 8 :
	        self.username += letters[letters_index]
             
            elif event.key == K_LEFT :
	      if self.username :
		saved=letters.index(self.username[-1])
		self.username= self.username[0:-1]
		letters_index=saved
		letters_display=letters[letters_index]
	    elif event.key == K_RETURN :
	      self.username += letters[letters_index]

	      user_to_register=Username(self.username,game_control.apple_counter,game_control.apples_total,float(self.percent_apples_eat_string))
	   
	      highscore.register_highscore(user_to_register,self.level)
	      run=False
	      self.show_highscore(self.level)
	   
           
      pygame.display.update() 
   
  def show_highscore(self,level_n) :
    global screen,level,phantoms_entities,snake,playground,game_control,animation_sounds,game_text,highscore
 
    pygame.display.set_caption("SnakeByte")
    pygame.display.set_icon(self.iconfy_icon)
 
    screen=pygame.display.set_mode((980, 680),0,32)
 
    level=Level(self.levels_snale_start_orientation[level_n],self.levels_files_dir+self.levels_files[level_n])


    phantoms_entities=level.compute_phantoms()
 
    snake=Snake(level.get_start_snake_head_position(),level.compute_level_data('snake'))

    playground=Playground(level.compute_level_data('apples'),level.compute_level_data('barriers'),level.compute_level_data('exit'),self.levels_snake_colors[level_n],self.levels_background_colors[level_n])   
    playground.losing_compute_down_gradient()
    playground.barriers_color_inversing()
    playground.phantoms_color_inversing()
 
    pygame.mixer.music.stop()
    animation_sounds=Animations_sounds()
    animation_sounds.set_intro_music_start()
    pygame.mixer.music.set_volume(0.5)
 
    game_text=Game_text()
 
    game_control=Game_control(len(level.compute_level_data('apples')))
 
    highscore=Highscores()
    self.highscore_display_color=(255,255,255,255)
    self.highscores_list=highscore.get_highscores(level_n)
    self.highscores_list.reverse()

    run=True
    index=0
    while run :
      screen.fill(playground.background_color)
      playground.draw_playground()
      screen.blit(game_text.little_font.render("|>--------  HIGHSCORES  --------<|",True,self.highscore_display_color),( ((980/2)-game_text.little_font.size("|>--------  HIGHSCORES  --------<|")[0]/2),game_text.little_font.size("|>--------  HIGHSCORES  --------<|")[1]/2))
      self.display_highscores(index)
      for event in pygame.event.get() :
	   
	  if event.type == QUIT :
	    exit()
	  if event.type == KEYDOWN :
	    if event.key == K_DOWN :
	      index += 1
	      if index == len(self.highscores_list) :
		index=index-1
            elif event.key == K_UP :
	      index -= 1
	      if index == -1 :
		index=0
	    elif event.key == K_ESCAPE :
	      run=False
	      game_mainloop.start_game_animation()
	   

      pygame.display.update()
   
  def display_highscores(self,idx) :
    self.highscore_line_x=128-32
    self.highscore_line_y=32+64
    self.highscore_displaying_scroll_index=idx
    for v in self.highscores_list :
      if self.highscore_displaying_scroll_index < len(self.highscores_list) :
	screen.blit(game_text.highscores_font.render(self.highscores_list[self.highscore_displaying_scroll_index][0]+(16-len(self.highscores_list[self.highscore_displaying_scroll_index][0])-1)*"-"+">"+str(self.highscores_list[self.highscore_displaying_scroll_index][2]).zfill(2)+"/"+str(self.highscores_list[self.highscore_displaying_scroll_index][3]),True,self.highscore_display_color),(self.highscore_line_x,self.highscore_line_y))
	self.highscore_line_y += 64
	self.highscore_displaying_scroll_index += 1
 
if __name__ == '__main__' :
  game_mainloop_control=Game_mainloop_control()
  game_mainloop=Game_mainloop()

  game_mainloop.start_game_animation()
