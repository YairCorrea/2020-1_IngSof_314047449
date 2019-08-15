#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SortOfPointlessDoublyLinkedList.py
#  
#  Copyright 2019 Maria Correa <computer@computer>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from list import List
class Node:
	def __init__(self,toStore,previousOne,nextOne):
		self.toStore=toStore
		self.previousOne=previousOne
		self.nextOne=nextOne
class DoublyLinkList(List):
	def __init__(self):
		self.head = None
		self.tail = None
		self.size=0
	def add1(self,element):
		NewNode=Node(element,None,None)
		if self.head is None:
			self.head= NewNode
			self.tail=self.head
		else:
			NewNode.previousOne=self.tail
			self.tail.nextOne=NewNode
			self.tail=NewNode
		self.size+=1
	def add(self,element,index):
		NewNode=Node(element,None,None)
		if index==self.size+1:
			add1(element)
		elif index>self.size+1:
			raise Exception("Lo siento, pero el indice tiene que ser a lo mas el siguiente valor de la lista actual.")
		elif index ==1:
			self.head.previousOne=NewNode
			NewNode.nextOne=self.head
			self.head=NewNode
		else:
			temporal=self.head
			for x in range(index-1):
				temporal=temporal.nextOne
			NewNode.previousOne=temporal
			NewNode.nextOne=temporal.nextOne
			temporal.nextOne=NewNode
			NewNode.nextOne.previousOne=NewNode
		self.size+=1
	def clear(self):
		self.head=None
		self.tail=None
		self.size=0
	def contains(self,obj):
		tmp=self.head
		while not tmp is None:
			if tmp.toStore is obj:
				return True
			tmp=tmp.nextOne
		return False
	def get(self,index):
		if index > self.size:
			return None
		if index < 1:
			return None
		indice=1
		tmp=self.head
		while indice<index:
			tmp=tmp.nextOne
			indice+=1
		return tmp.toStore
	def isEmpty(self):
		return self.size is 0
	def remove1(self,index):
		if index > self.size:
			return None
		if index < 1:
			return None
		indice=1
		tmp=self.head
		while indice<index:
			tmp=tmp.nextOne
			indice+=1
		if not tmp is self.tail:
			tmp.nextOne.previousOne=tmp.previousOne
		else:
			self.tail=tmp.previousOne
		if not tmp is self.head:
			tmp.previousOne.nextOne=tmp.nextOne
		else:
			self.head=tmp.nextOne
		self.size+=-1
		return tmp.toStore
	def remove(self,obj):
		tmp=self.head
		ind=1
		while not tmp is None:
			if tmp.toStore is obj:
				return remove1(ind)
			tmp=tmp.nextOne
			ind+=1
		return None
	def Size(self):
		return self.size		
	def toArray(self):
		arreglo=[]
		tmp=self.head
		while not tmp is None:
			arreglo.append(tmp.toStore)
			tmp=tmp.nextOne
		return arreglo
