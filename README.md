#CA Simulations

This repo will be used for developing cellular automata simulations for the Geeni business model, and to give
us better data and benchmarks of how elements in the business will play out. This readme contains a background on
automata, and subsequently, cellular automata.

##Tutorial

Cellular Automata, are groups of small, simple, abstract machines. There are two components to understanding them, their arrangement, in an algebraic structure called a lattice, and what an automata is. I will go over both.

###Lattice

A cellular automata, are many, many tiny machines, arranged in a network called a lattice. A lattice, is a linked network of values, where every element, has some higher order element, and lower order element associated with it. Secondly, each higher and order element is unique to one another.

One example from math, are the order of integers. Every integer, has some least common multiple, and greatest common divisor. These can be though of as a join, the upper bound, and a meet, the lower bound.

Lets try out an example in python.

```
#turns a string into a partiallty ordered set

def toPartSet(string):
	pset = set({})
	for i in range(len(string)-1):
		pset.add(string[i] + "->" + string[i+1])
	return pset
	
print(toPartSet("hello world!"))
```

which results in:

```
{'r->l', 'd->!', ' ->w', 'l->d', 'h->e', 'l->l', 'w->o', 'e->l', 'o->r', 'o-> ', 'l->o'}
```
This example, takes a string, `"hello world!"` and forms it into a partially ordered set, where each element has some higher and lower value associated with it. However, this is not a lattice. Multiple letters have a join at l,  where in a lattice, every two elements must have a unique join and meet.

###Automata

An automata, is an abstract concept of a machine, one which takes some input instructions, and based on whether or not those instructions are known, it will change it's state. An easy example for an automata is a light switch. It has two states, `on` and `off`. It has two possible instructions, flip up, and flip down. In it's off state, it can only accept the instruction flip up, to go to the on state. Inputting the flip down instruction in the off phase has no effect. Lets look at this example in Python:

```
#modeling of a light switch

class LightSwitch:
	
	def __init__(self):
		self.state = "off"
		self.accepting = "flip_up"
	def giveInstruction(self, input):
		if input == self.accepting:
			self.state = "on"
			self.accepting = "flip_down"
			return "state changed"
		else:
			return "no effect"
			
"""=> None
   f = LightSwitch()
=> None
   f
=> <LightSwitch object at 0x7f3b723bdc88>
   f.giveInstruction("flip_up")
=> 'state changed'
   f.giveInstruction("flip_down")
=> 'state changed'"""
```