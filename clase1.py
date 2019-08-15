#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  clase1.py
#  
#  Copyright 2019 Yair Correa
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
class Class1:
	def __init__(self, foo, bar):
			self.foo = foo
			self.bar = bar
	def multFoo(self):
			stuff=":) "
			for x in range(self.foo):
				stuff+="foo"
				for y in range(self.bar):
					stuff+="o"
				stuff+="bar \n"
			sys.stdout.write(stuff)
			
def main(args):
	print("No se me ocurrio nada en realidad, asi que esta esta cosa que ya de perdida espero le resulte chistosa.")
	print("Teclea un numero a continuacion")
	coso1=int(raw_input('->'))
	print("Y uno mas")
	coso2=int(raw_input('->'))
	foo= (Class1(coso1,coso2)) if (coso1 > 0 and coso2 > 0) else (Class1(666,666))
	foo.multFoo()
        print("Y medio checa la lista ligada")
        lista=DoublyLinkList()
        lista.add1(666)
        lista.add1(1332)
        lista.add1(1998)
        print(lista.toArray())
        lista.add(2664,2)
        print(lista.toArray())
        print(lista.get(3))
        siz=lista.Size()
        while not lista.isEmpty():
            lista.remove1(siz)
            siz+=-1
        print(lista.toArray())
if __name__ == '__main__':
    import sys
    from SortOfPointlessDoublyLinkedList import DoublyLinkList
    sys.exit(main(sys.argv))
