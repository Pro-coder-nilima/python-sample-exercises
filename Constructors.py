
'''
Constructor :Initializing the object variable .
       instance -->object
       instances -->insatnce variables(obj ralated value)
       instantiation --> creating of an obj.	
       initialization --> assigning some value.
self --> self is a keyword, used to refers the current object.
'''

class student:
	def __init__(self,name,id):
		self.name = name;           # instance variables
		self.id = id;
		def display(self):          #instance method
			pass
s = student('suthi',10)
print(s.name,s.id)

