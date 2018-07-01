#1

class Animal:
   def animal_attribute(self):
      print("Animal class called")

class Tiger(Animal):
   pass

x = Animal()
x.animal_attribute()

#2
with python2 
output ->  A g

with python 3 there is an error because in the last line instead of
print a.f(),b.f() there should be
print(a.f(),b.f()) then only the same output will come.


#3
class Cop:
   def add(self, name, age,work, experience, designation):
      self.name = name
      self.age = age
      self.work = work
      self.experience = experience
      self.designation = designation

   def display(self):
      print("Name: ",self.name)
      print("Age: ",self.age)
      print("Work: ",self.work)
      print("Experience: ",self.experience)
      print("Designation: ",self.designation)

   def update(self, u_name, u_age, u_experience, u_designation):
      self.name = u_name
      self.age = u_age
      self.work = u_work
      self.experience = u_experience
      self.designation = u_designation

class Mission(Cop):
   def add_mission_details(self, mission):
      self.mission = mission
      print("Mission: ",self.mission)

x = Mission()
x.add("Clay",21,"Supervision", 5, "IAS")
x.display()
x.add_mission_details("control robbery")


#4


class Shape:
   
   def __init__(self, length, breadth):
      self.length = length
      self.breadth = breadth

   def Area(self):
      self.area = self.length*self.breadth
      print("Area: ",self.area)

class Square(Shape):
   print("Square")
   

class Rectangle(Shape):
   print("Rectangle")
   

x = Square(4,4)
x.Area()
y = Rectangle(5,6)
y.Area()
